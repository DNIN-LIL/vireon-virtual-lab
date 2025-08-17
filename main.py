import argparse
import importlib.util
import os
import sys
from pathlib import Path

from core.config_loader import load_config
from core.medium import Medium


REPO_ROOT = Path(__file__).resolve().parent
EXP_ROOT = REPO_ROOT / "experiments"
MEDIUMS_DIR = REPO_ROOT / "mediums"


def find_experiments():
    items = []
    if not EXP_ROOT.exists():
        return items
    for p in sorted(EXP_ROOT.iterdir()):
        if not p.is_dir():
            continue
        logic = p / "logic.py"
        if logic.exists():
            items.append(p)
    return items


def load_logic_module(exp_dir: Path):
    logic_path = exp_dir / "logic.py"
    name = f"exp_{exp_dir.name}"
    spec = importlib.util.spec_from_file_location(name, str(logic_path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {logic_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def default_medium_for(exp_name: str) -> str:
    if "plasma" in exp_name.lower():
        return "plasma.yaml"
    return "vacuum.yaml"


def list_available_mediums():
    out = []
    if MEDIUMS_DIR.exists():
        for p in sorted(MEDIUMS_DIR.glob("*.y*ml")):
            out.append(p.name)
    return out


def prompt(msg: str, default=None):
    if default is None:
        s = input(f"{msg}: ").strip()
        return s
    s = input(f"{msg} [{default}]: ").strip()
    return s if s else str(default)


def parse_scalar(val: str):
    v = val.strip()
    if v.lower() in ("none", "null"):
        return None
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    try:
        if v.lower().startswith(("0x", "0b")):
            return int(v, 0)
        if any(ch in v for ch in (".", "e", "E")):
            return float(v)
        return int(v)
    except Exception:
        return v


def parse_list(val: str):
    parts = [x.strip() for x in val.split(",") if x.strip()]
    out = []
    for p in parts:
        out.append(parse_scalar(p))
    return out


def stringify(value):
    if isinstance(value, (list, tuple)):
        return ", ".join(str(x) for x in value)
    return value


def interactive_edit(cfg: dict):
    print("\nEnter to keep defaults. Use comma-separated values for lists.")
    keys = [k for k in cfg.keys()]
    for k in keys:
        v = cfg.get(k)
        if isinstance(v, dict):
            continue
        shown = stringify(v)
        inp = prompt(f"{k}", shown)
        if inp == str(shown) or inp == "" and shown is not None:
            continue
        if "," in inp:
            cfg[k] = parse_list(inp)
        else:
            cfg[k] = parse_scalar(inp)

    print("\nAdd additional parameters (key=value). Leave blank to continue.")
    while True:
        line = input("> ").strip()
        if not line:
            break
        if "=" not in line:
            print("Format is key=value")
            continue
        key, val = [s.strip() for s in line.split("=", 1)]
        if "," in val:
            cfg[key] = parse_list(val)
        else:
            cfg[key] = parse_scalar(val)
    return cfg


def choose_experiment(experiments):
    print("\nAvailable experiments:\n")
    for i, p in enumerate(experiments, 1):
        print(f"  {i}. {p.name}")
    while True:
        sel = input("\nSelect experiment by number (or name): ").strip()
        if not sel:
            continue
        if sel.isdigit():
            idx = int(sel) - 1
            if 0 <= idx < len(experiments):
                return experiments[idx]
        else:
            for p in experiments:
                if p.name.lower() == sel.lower():
                    return p
        print("Invalid selection.")


def build_medium(medium_name_or_path: str, cfg: dict):
    if not medium_name_or_path:
        medium_name_or_path = default_medium_for(cfg.get("__exp_name__", ""))

    path = Path(medium_name_or_path)
    if not path.suffix and MEDIUMS_DIR.exists():
        candidate = MEDIUMS_DIR / medium_name_or_path
        if candidate.with_suffix(".yaml").exists():
            path = candidate.with_suffix(".yaml")
        elif candidate.with_suffix(".yml").exists():
            path = candidate.with_suffix(".yml")

    if path.exists():
        mcfg = load_config(str(path))
    else:
        mcfg = {"name": medium_name_or_path}

    return Medium({"medium": mcfg})


def run_experiment(exp_dir: Path, cfg_overrides: dict | None, medium_choice: str | None, no_prompt: bool):
    cfg_path = exp_dir / "config.yaml"
    base_cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    base_cfg["__exp_name__"] = exp_dir.name

    cfg = dict(base_cfg)
    if cfg_overrides:
        cfg.update(cfg_overrides)

    if not no_prompt:
        print(f"\nEditing parameters for {exp_dir.name}")
        cfg = interactive_edit(cfg)

    default_medium = default_medium_for(exp_dir.name)
    available = list_available_mediums()
    shown = medium_choice if medium_choice else default_medium
    if not no_prompt:
        if available:
            print("\nMediums found:")
            for m in available:
                print(f"  - {m}")
        shown = prompt("Medium file name or path", shown)

    medium = build_medium(shown, cfg)

    try:
        logic = load_logic_module(exp_dir)
        if hasattr(logic, "run"):
            try:
                result = logic.run(cfg, medium)
            except TypeError:
                try:
                    result = logic.run(cfg)
                except TypeError:
                    result = logic.run()
        elif hasattr(logic, "run_noargs"):
            result = logic.run_noargs()
        else:
            raise RuntimeError("logic.py has no run() or run_noargs()")
    except Exception as e:
        print("\nExperiment failed.")
        print(f"{type(e).__name__}: {e}")
        raise
    else:
        print("\nExperiment completed.")
        if isinstance(result, dict):
            for k, v in result.items():
                print(f"{k}: {v}")
    return 0


def parse_overrides(kv_list):
    out = {}
    if not kv_list:
        return out
    for item in kv_list:
        if "=" not in item:
            continue
        key, val = item.split("=", 1)
        key = key.strip()
        val = val.strip()
        if "," in val:
            out[key] = parse_list(val)
        else:
            out[key] = parse_scalar(val)
    return out


def main():
    parser = argparse.ArgumentParser(description="Vireon Terminal Interface")
    parser.add_argument("--exp", help="experiment folder name (under experiments/)")
    parser.add_argument("--medium", help="medium yaml name or path (e.g., plasma.yaml)")
    parser.add_argument("--set", nargs="*", help="override parameters as key=value", dest="overrides")
    parser.add_argument("--no-prompt", action="store_true", help="run without interactive prompts")

    args = parser.parse_args()
    experiments = find_experiments()
    if not experiments:
        print("No experiments found.")
        return 1

    if args.exp:
        exp_dir = EXP_ROOT / args.exp
        if not exp_dir.exists():
            print(f"Experiment not found: {args.exp}")
            return 1
    else:
        exp_dir = choose_experiment(experiments)

    overrides = parse_overrides(args.overrides)
    return run_experiment(exp_dir, overrides, args.medium, args.no_prompt)


if __name__ == "__main__":
    sys.exit(main())
