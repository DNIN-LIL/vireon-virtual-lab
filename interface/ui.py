import sys
import io
import threading
import importlib
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from core.engine.lab_runner import run_experiment

# ---------- Discovery ----------

def _module_exists(module_path: str) -> bool:
    try:
        importlib.import_module(module_path)
        return True
    except ModuleNotFoundError:
        return False

def _has_callable(module_path: str, names):
    if not _module_exists(module_path):
        return None
    mod = importlib.import_module(module_path)
    for n in names:
        if hasattr(mod, n):
            return getattr(mod, n)
    return None

def _iter_experiment_targets():
    """
    Yields experiment targets (strings) relative to experiments/,
    supporting both root orchestrators and sub-experiments with config.yaml.
    """
    root = Path("experiments")
    if not root.exists():
        return

    for top in sorted(p for p in root.iterdir() if p.is_dir()):
        # Root orchestrator?
        run_all = top / "run_all.py"
        logic_root = top / "logic.py"
        top_name = top.name
        mod_base = "experiments." + top_name

        if run_all.exists() and _has_callable(mod_base + ".run_all", ("run_all", "main")):
            yield top_name
            continue
        if logic_root.exists() and _has_callable(mod_base + ".logic", ("run", "main", "run_all")):
            yield top_name
            # still also include sub-experiments if configs present
        # Sub-experiments with config.yaml
        for child in sorted(p for p in top.iterdir() if p.is_dir()):
            cfg = child / "config.yaml"
            if cfg.exists():
                rel = child.relative_to(root).as_posix()
                yield rel

def _collect_targets():
    seen = set()
    out = []
    for name in _iter_experiment_targets():
        if name not in seen:
            out.append(name)
            seen.add(name)
    return out

# ---------- Runner (mirrors main.run_exp logic) ----------

def _import_and_call(module_path: str, fn_candidates=("run_all", "main", "run")):
    if not _module_exists(module_path):
        return False
    mod = importlib.import_module(module_path)
    for fn in fn_candidates:
        if hasattr(mod, fn):
            getattr(mod, fn)()
            return True
    return False

def _run_exp_like_main(exp_name: str, log_write=lambda *_: None):
    exp_dir = Path("experiments") / exp_name
    if exp_dir.is_dir():
        run_all_mod = "experiments." + exp_name.replace("/", ".").replace("\\", ".") + ".run_all"
        logic_root_mod = "experiments." + exp_name.replace("/", ".").replace("\\", ".") + ".logic"

        if (exp_dir / "run_all.py").exists() and _import_and_call(run_all_mod, ("run_all", "main")):
            return

        if (exp_dir / "logic.py").exists() and _import_and_call(logic_root_mod, ("run", "main", "run_all")):
            return

        sub_ran = False
        for child in sorted(exp_dir.iterdir()):
            if (child / "config.yaml").exists():
                rel = child.relative_to(Path("experiments")).as_posix()
                log_write(f"Running sub-experiment: {rel}\n")
                run_experiment(rel)
                sub_ran = True
        if sub_ran:
            return

    # Fallback: treat as sub-experiment
    log_write(f"Running experiment: {exp_name}\n")
    run_experiment(exp_name.replace("\\", "/"))

# ---------- Tk UI ----------

class TextRedirector(io.TextIOBase):
    def __init__(self, widget, tag=None):
        self.widget = widget
        self.tag = tag

    def write(self, s):
        self.widget.configure(state="normal")
        self.widget.insert("end", s)
        self.widget.see("end")
        self.widget.configure(state="disabled")
        return len(s)

    def flush(self):
        pass

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vireon Virtual Lab")
        self.geometry("900x600")

        self.targets = _collect_targets()

        self._build_widgets()
        self._populate_targets()

        self.worker = None
        self.stop_flag = False

    def _build_widgets(self):
        frame_top = ttk.Frame(self)
        frame_top.pack(side="top", fill="x", padx=10, pady=10)

        ttk.Label(frame_top, text="Experiment:").pack(side="left")
        self.combo = ttk.Combobox(frame_top, state="readonly", width=60, values=[])
        self.combo.pack(side="left", padx=8)
        if self.targets:
            self.combo.set(self.targets[0])

        btn_run = ttk.Button(frame_top, text="Run Selected", command=self._on_run)
        btn_run.pack(side="left", padx=6)

        btn_refresh = ttk.Button(frame_top, text="Refresh", command=self._on_refresh)
        btn_refresh.pack(side="left", padx=6)

        btn_open = ttk.Button(frame_top, text="Open Output...", command=self._on_open_output)
        btn_open.pack(side="left", padx=6)

        frame_log = ttk.Frame(self)
        frame_log.pack(side="top", fill="both", expand=True, padx=10, pady=(0,10))

        self.text = tk.Text(frame_log, wrap="word", state="disabled")
        self.text.pack(side="left", fill="both", expand=True)

        scroll = ttk.Scrollbar(frame_log, command=self.text.yview)
        scroll.pack(side="right", fill="y")
        self.text["yscrollcommand"] = scroll.set

    def _populate_targets(self):
        self.targets = _collect_targets()
        self.combo["values"] = self.targets
        if self.targets and not self.combo.get():
            self.combo.set(self.targets[0])

    def _append_log(self, s: str):
        self.text.configure(state="normal")
        self.text.insert("end", s)
        self.text.see("end")
        self.text.configure(state="disabled")

    def _on_refresh(self):
        self._populate_targets()
        self._append_log("Refreshed experiment list.\n")

    def _on_open_output(self):
        base = Path("output")
        if not base.exists():
            messagebox.showinfo("Output", "No output directory yet.")
            return
        filedialog.askopenfilename(initialdir=str(base), title="Browse outputs")
        # The dialog itself is sufficient as a quick way to jump to the folder.

    def _on_run(self):
        if self.worker and self.worker.is_alive():
            messagebox.showwarning("Busy", "A run is already in progress.")
            return
        target = self.combo.get().strip()
        if not target:
            messagebox.showwarning("No selection", "Select an experiment to run.")
            return

        self._append_log(f"Starting: {target}\n")

        # Run on a background thread and capture stdout/stderr into the log.
        def worker():
            old_out, old_err = sys.stdout, sys.stderr
            sys.stdout = TextRedirector(self.text)
            sys.stderr = TextRedirector(self.text)
            try:
                _run_exp_like_main(target, log_write=self._append_log)
                self._append_log(f"Finished: {target}\n")
            except Exception as e:
                self._append_log(f"Error: {e}\n")
            finally:
                sys.stdout, sys.stderr = old_out, old_err

        self.worker = threading.Thread(target=worker, daemon=True)
        self.worker.start()

def launch():
    app = App()
    app.mainloop()
