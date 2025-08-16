import argparse
import importlib
from pathlib import Path
from core.engine.lab_runner import run_experiment

def _module_exists(module_path: str) -> bool:
    try:
        importlib.import_module(module_path)
        return True
    except ModuleNotFoundError:
        return False

def _import_and_call(module_path: str, fn_candidates=("run_all", "main", "run")):
    mod = importlib.import_module(module_path)
    for fn in fn_candidates:
        if hasattr(mod, fn):
            getattr(mod, fn)()
            return True
    return False

def run_exp(exp_name: str):
    """
    Accepts either an experiment root (e.g. "magnetic_oscillation")
    or a sub-experiment (e.g. "magnetic_oscillation/vacuum_sine").
    """
    exp_dir = Path("experiments") / exp_name
    if exp_dir.is_dir():
        # Prefer a root orchestrator if present: run_all.py or logic.py with a callable.
        run_all_mod = "experiments." + exp_name.replace("/", ".").replace("\\", ".") + ".run_all"
        logic_root_mod = "experiments." + exp_name.replace("/", ".").replace("\\", ".") + ".logic"

        if (exp_dir / "run_all.py").exists() and _module_exists(run_all_mod):
            _import_and_call(run_all_mod, ("run_all", "main"))
            return

        if (exp_dir / "logic.py").exists() and _module_exists(logic_root_mod):
            # Allow root logic orchestrators that expose run()/main()
            if _import_and_call(logic_root_mod, ("run", "main", "run_all")):
                return

        # Otherwise, if subfolders exist with config.yaml, run each as a sub-experiment.
        sub_ran = False
        for child in sorted(exp_dir.iterdir()):
            if (child / "config.yaml").exists():
                rel = str(child.relative_to(Path("experiments")))
                run_experiment(rel.replace("\\", "/"))
                sub_ran = True
        if sub_ran:
            return

    # Fallback: treat exp_name as a sub-experiment path.
    run_experiment(exp_name.replace("\\", "/"))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--exp")
    args = ap.parse_args()
    if args.exp:
        run_exp(args.exp)
    else:
        from interface.ui import launch
        launch()
