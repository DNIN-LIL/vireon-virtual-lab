import importlib
from pathlib import Path
from typing import Optional, Tuple, Dict, Any
from core.config_loader import load_config
from core.medium import Medium

def _module_path_for(exp_name: str) -> str:
    # "magnetic_oscillation/vacuum_sine" -> "experiments.magnetic_oscillation.vacuum_sine.logic"
    return "experiments." + exp_name.replace("/", ".").replace("\\", ".") + ".logic"

def _config_path_for(exp_name: str) -> Path:
    return Path("experiments") / exp_name / "config.yaml"

def _load_cfg_and_medium(exp_name: str) -> Tuple[Dict[str, Any], Medium]:
    cfg_path = _config_path_for(exp_name)
    cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    # Allow either nested `medium: {...}` or top-level flat keys:
    medium_cfg = {"medium": cfg.get("medium", cfg)}
    medium = Medium(medium_cfg)
    return cfg, medium

def run_experiment(exp_name: str):
    """
    Load experiments/<exp_name>/logic.py and call run(cfg, medium).
    """
    mod_path = _module_path_for(exp_name)
    module = importlib.import_module(mod_path)
    if not hasattr(module, "run"):
        raise RuntimeError(f"No run() in {mod_path}")

    cfg, medium = _load_cfg_and_medium(exp_name)

    # Prefer headless signature run(cfg, medium); if a legacy no-arg exists, call it.
    try:
        return module.run(cfg, medium)
    except TypeError:
        return module.run()
