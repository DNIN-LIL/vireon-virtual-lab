import sys
import importlib
import importlib.util
from pathlib import Path
from typing import Iterable

from core.config_loader import load_config
from core.medium import Medium

SUBEXPS = {
    "vacuum": ["vacuum_sine", "vacuum_square", "vacuum_triangle"],
    "plasma": ["plasma_sine", "plasma_square", "plasma_triangle"],
}

PKG_FALLBACK = "experiments.z_magnetic_oscillation"


def _pkg_base() -> str:
    if __package__:
        return __package__
    return PKG_FALLBACK


def _to_str_list(val) -> list[str]:
    if val is None:
        return []
    if isinstance(val, (list, tuple)):
        return [str(x).strip().lower() for x in val if str(x).strip()]
    return [s.strip().lower() for s in str(val).split(",") if s.strip()]


def _wave_filter(all_names: Iterable[str], cfg: dict) -> list[str]:
    waves = _to_str_list(cfg.get("waveforms"))
    if not waves and cfg.get("waveform"):
        wf = str(cfg.get("waveform")).strip().lower()
        waves = ["sine", "square", "triangle"] if wf == "all" else [wf]
    if not waves:
        return list(all_names)
    keep = set(waves)
    out = []
    for name in all_names:
        if any(name.endswith(suf) for suf in keep):
            out.append(name)
    return out or list(all_names)


def _merge_overrides(base: dict, overrides: dict) -> dict:
    if not overrides:
        return dict(base)
    merged = dict(base)
    for k, v in overrides.items():
        if k == "medium":
            continue
        merged[k] = v
    return merged


def _import_child_abs(pkg_base: str, child_name: str):
    mod_name = f"{pkg_base}.{child_name}.logic"
    return importlib.import_module(mod_name)


def _import_child_from_file(child_dir: Path, child_name: str):
    file = child_dir / "logic.py"
    mod_name = f"{PKG_FALLBACK}.{child_name}.logic"
    spec = importlib.util.spec_from_file_location(mod_name, file)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load spec for {file}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = mod
    spec.loader.exec_module(mod)
    return mod


def _load_child_cfg(child_dir: Path) -> dict:
    cfg_path = child_dir / "config.yaml"
    return load_config(str(cfg_path)) if cfg_path.exists() else {}


def _call_child(mod, cfg: dict, medium: Medium):
    if hasattr(mod, "run"):
        try:
            return mod.run(cfg, medium)
        except TypeError:
            return mod.run(cfg)
    if hasattr(mod, "run_noargs"):
        return mod.run_noargs()
    raise RuntimeError(f"{mod.__name__} has no run() or run_noargs()")


def run(cfg=None, medium: Medium | None = None, *args, **kwargs):
    if medium is None:
        raise ValueError("medium is required")

    cfg = cfg or {}
    base_dir = Path(__file__).resolve().parent
    pkg_base = _pkg_base()

    medium_key = str(getattr(medium, "type", "vacuum")).lower()
    child_names = SUBEXPS.get(medium_key, [])
    child_names = _wave_filter(child_names, cfg)

    ran = []
    failures = []

    for name in child_names:
        child_dir = base_dir / name
        try:
            mod = _import_child_abs(pkg_base, name)
        except Exception as e1:
            try:
                mod = _import_child_from_file(child_dir, name)
            except Exception as e2:
                failures.append({"child": name, "error": f"import failed: {e1 or e2}"})
                continue

        child_cfg = _load_child_cfg(child_dir)
        eff_cfg = _merge_overrides(child_cfg, cfg)
        eff_cfg["__child_name__"] = name

        try:
            out = _call_child(mod, eff_cfg, medium)
            ran.append({"child": name, "result": out})
        except Exception as e:
            failures.append({"child": name, "error": str(e)})

    return {
        "medium": medium_key,
        "ran": [r["child"] for r in ran],
        "failed": failures,
        "count_ok": len(ran),
        "count_fail": len(failures),
        "base_dir": str(base_dir),
    }


def run_noargs():
    m = Medium({"type": "vacuum"})
    return run({}, m)
