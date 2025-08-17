import os
from pathlib import Path
import math

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from core.medium import Medium
from core.config_loader import load_config


def _ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def _to_float_list_flexible(val):
    if val is None:
        return []
    if isinstance(val, (list, tuple)):
        items = list(val)
    else:
        items = [x.strip() for x in str(val).split(",")]
    out = []
    for x in items:
        if x == "":
            continue
        out.append(float(x))
    return out


def _get_list(cfg: dict, list_key: str, scalar_key: str, default_list):
    lst = _to_float_list_flexible(cfg.get(list_key))
    if lst:
        return lst
    lst = _to_float_list_flexible(cfg.get(scalar_key))
    if lst:
        return lst
    return list(default_list)


def _as_float(val, default: float) -> float:
    if val is None:
        return float(default)
    return float(val)


def _dt_from_sampling(cfg: dict, medium: Medium) -> float:
    sr = float(cfg.get("sampling_rate", 0.0))
    if sr > 0.0:
        return 1.0 / sr
    dt_raw = getattr(medium, "dt", None)
    if dt_raw is None:
        raise ValueError("medium.dt is missing; set sampling_rate or define medium.dt")
    dt = float(dt_raw)
    if dt <= 0.0:
        raise ValueError(f"medium.dt must be > 0 (got {dt})")
    return dt


def _load_cfg_if_needed(cfg):
    if isinstance(cfg, dict) or cfg is None:
        return cfg or {}
    p = Path(str(cfg))
    if p.suffix.lower() in (".yml", ".yaml") and p.exists():
        return load_config(str(p))
    return {}


def _normalize_args(cfg, medium, args):
    if isinstance(cfg, str):
        if args:
            cfg, medium = args[0], (args[1] if len(args) > 1 else medium)
        else:
            cfg_path = Path(__file__).resolve().parent / "config.yaml"
            cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    cfg = _load_cfg_if_needed(cfg)
    return cfg, medium


def _plasma_scale(cfg: dict, medium: Medium) -> float:
    base = _as_float(cfg.get("plasma_scale"), 1.0)
    props = getattr(medium, "properties", None)
    if isinstance(props, dict):
        if props.get("screening_factor") is not None:
            return _as_float(props.get("screening_factor"), base)
        if "relative_permittivity" in props and "plasma_scale" not in cfg:
            try:
                eps_r = float(props["relative_permittivity"])
                if eps_r > 1.0:
                    return base * eps_r
            except Exception:
                pass
    return base


def _attenuation_for_freq(f_hz: float, cfg: dict, medium: Medium) -> float:
    # Simple collisional attenuation: 1 / sqrt(1 + (nu/omega)^2)
    nu = _as_float(cfg.get("collision_freq"), float(getattr(getattr(medium, "properties", {}), "get", lambda *_: 0.0)("collision_freq", 0.0)))
    omega = 2.0 * math.pi * float(f_hz)
    if omega <= 0.0:
        return 1.0
    return 1.0 / math.sqrt(1.0 + (nu / omega) ** 2)


def run(cfg=None, medium: Medium | None = None, *args, **kwargs):
    cfg, medium = _normalize_args(cfg, medium, list(args))
    if medium is None:
        raise ValueError("medium is required")

    Q = _as_float(cfg.get("charge"), 1e-6)
    f_hz = _as_float(cfg.get("frequency_hz"), 1.0e6)
    masses = _get_list(cfg, "masses", "mass", [0.1, 0.5, 1.0, 5.0, 10.0])
    k_const = _as_float(cfg.get("default_k"), 1.0)
    duration_s = _as_float(cfg.get("duration_s"), 1.0)
    out_dir = cfg.get("output_dir", "output/mass_scaling_at_constant_qf_in_plasma")

    _ensure_dir(out_dir)
    dt = _dt_from_sampling(cfg, medium)
    steps = max(1, int(duration_s / dt))

    scale = _plasma_scale(cfg, medium) * _attenuation_for_freq(f_hz, cfg, medium)

    masses = np.array([float(m) for m in masses], dtype=float)
    force = k_const * Q * f_hz * masses * scale
    accel = np.divide(force, masses, out=np.full_like(masses, k_const * Q * f_hz * scale), where=masses != 0.0)

    data = np.column_stack([masses, force, accel])
    np.savetxt(
        os.path.join(out_dir, "mass_force_accel.csv"),
        data,
        delimiter=",",
        fmt="%.6e",
        header="mass,force,accel"
    )

    fig, ax = plt.subplots()
    ax.plot(masses, force, marker="o")
    ax.set_xlabel("Mass")
    ax.set_ylabel("Force (N)")
    ax.set_title("Force vs Mass at constant Q·f (plasma)")
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, "force_vs_mass.png"))
    plt.close(fig)

    fig2, ax2 = plt.subplots()
    ax2.plot(masses, accel, marker="o")
    ax2.set_xlabel("Mass")
    ax2.set_ylabel("Acceleration (m/s^2)")
    ax2.set_title("Acceleration vs Mass (plasma)")
    ax2.grid(True)
    fig2.tight_layout()
    fig2.savefig(os.path.join(out_dir, "accel_vs_mass.png"))
    plt.close(fig2)

    np.savez(
        os.path.join(out_dir, "results.npz"),
        masses=masses,
        force=force,
        accel=accel,
        Q=Q,
        f_hz=f_hz,
        k=k_const,
        scale=scale,
        dt=dt,
        steps=steps,
    )

    return {
        "steps": steps,
        "dt": dt,
        "output_dir": out_dir,
        "points": len(masses),
        "Q": Q,
        "f_hz": f_hz,
        "k": k_const,
        "plasma_scale": scale,
    }


def run_noargs():
    cfg_path = Path(__file__).resolve().parent / "config.yaml"
    cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    medium = Medium({"medium": cfg.get("medium", cfg)})
    return run(cfg, medium)
