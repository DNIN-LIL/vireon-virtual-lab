import os
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from core.medium import Medium
from core.config_loader import load_config


def _ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def _to_float_list(val, name: str):
    if val is None:
        raise ValueError(f"Missing required list '{name}' in config.yaml")
    if isinstance(val, str):
        parts = [x.strip() for x in val.split(",") if x.strip()]
    else:
        parts = list(val)
    out = []
    for x in parts:
        try:
            out.append(float(x))
        except Exception as e:
            raise ValueError(f"Non-numeric entry in '{name}': {x!r}") from e
    if not out:
        raise ValueError(f"Empty list for '{name}' after parsing")
    return out


def _as_float(val, name: str, default: float):
    if val is None:
        return float(default)
    try:
        return float(val)
    except Exception as e:
        raise ValueError(f"'{name}' must be numeric (got {val!r})") from e


def _dt_from_sampling(cfg: dict, medium: Medium) -> float:
    sr_raw = cfg.get("sampling_rate", 0.0)
    try:
        sr = float(sr_raw)
    except Exception:
        raise ValueError(f"sampling_rate must be numeric (got {sr_raw!r})")

    if sr > 0.0:
        return 1.0 / sr

    dt_raw = getattr(medium, "dt", None)
    if dt_raw is None:
        raise ValueError("medium.dt is missing; set sampling_rate or define medium.dt")
    try:
        dt = float(dt_raw)
    except Exception:
        raise ValueError(f"medium.dt must be numeric (got {dt_raw!r})")
    if dt <= 0.0:
        raise ValueError(f"medium.dt must be > 0 (got {dt})")
    return dt


def _plasma_scale(cfg: dict, medium: Medium) -> float:
    base = _as_float(cfg.get("plasma_scale"), "plasma_scale", 1.0)
    props = getattr(medium, "properties", None)
    if isinstance(props, dict) and props.get("screening_factor") is not None:
        return _as_float(props.get("screening_factor"), "screening_factor", base)
    return base


def _load_cfg_if_needed(cfg):
    if isinstance(cfg, dict) or cfg is None:
        return cfg or {}
    p = Path(str(cfg))
    if p.suffix.lower() in (".yml", ".yaml") and p.exists():
        return load_config(str(p))
    return {}


def _normalize_args(cfg, medium, args):
    # Accept: (cfg, medium), ("exp_name", cfg, medium), (cfg_path, medium), (cfg), ()
    if isinstance(cfg, str):
        if args:
            cfg, medium = args[0], (args[1] if len(args) > 1 else medium)
            args = args[2:]
        else:
            cfg_path = Path(__file__).resolve().parent / "config.yaml"
            cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    cfg = _load_cfg_if_needed(cfg)
    return cfg, medium, args


def run(cfg=None, medium: Medium | None = None, *args, **kwargs):
    cfg, medium, _ = _normalize_args(cfg, medium, list(args))
    if medium is None:
        raise ValueError("medium is required")

    charges = _to_float_list(cfg.get("charges"), "charges")
    freqs_hz = _to_float_list(cfg.get("frequencies"), "frequencies")
    mass = _as_float(cfg.get("mass"), "mass", 1.0)
    k = _as_float(cfg.get("default_k"), "default_k", 1.0)
    duration_s = _as_float(cfg.get("duration_s"), "duration_s", 1.0)
    out_dir = cfg.get("output_dir", "output/charge_frequency_sweep_in_plasma")

    _ensure_dir(out_dir)

    dt = _dt_from_sampling(cfg, medium)
    steps = max(1, int(duration_s / dt))

    scale_factor = _plasma_scale(cfg, medium)

    force_matrix = np.zeros((len(charges), len(freqs_hz)), dtype=float)
    for i, Q in enumerate(charges):
        Qi = float(Q)
        for j, f_hz in enumerate(freqs_hz):
            force_matrix[i, j] = k * Qi * float(f_hz) * mass * scale_factor

    np.savetxt(
        os.path.join(out_dir, "force_matrix.csv"),
        force_matrix,
        delimiter=",",
        fmt="%.6e",
    )

    fig, ax = plt.subplots()
    im = ax.imshow(force_matrix, cmap="plasma", origin="lower", aspect="auto")
    ax.set_xticks(np.arange(len(freqs_hz)))
    ax.set_yticks(np.arange(len(charges)))
    ax.set_xticklabels([f"{f:.0e}" for f in freqs_hz])
    ax.set_yticklabels([f"{q:.0e}" for q in charges])
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Charge (C)")
    ax.set_title("Plasma-Modified Force Magnitude (N)")
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, "force_matrix.png"))
    plt.close(fig)

    return {
        "steps": steps,
        "dt": dt,
        "output_dir": out_dir,
        "shape": force_matrix.shape,
        "plasma_scale": scale_factor,
    }


def run_noargs():
    cfg_path = Path(__file__).resolve().parent / "config.yaml"
    if not cfg_path.exists():
        raise FileNotFoundError(f"Config file not found: {cfg_path}")
    cfg = load_config(str(cfg_path))
    if not isinstance(cfg, dict):
        raise ValueError(f"Loaded config is {type(cfg)}, expected dict")
    medium_type = cfg.get("medium", "vacuum")  # Use string, not cfg as fallback
    medium = Medium({"medium": medium_type})
    return run(cfg, medium)