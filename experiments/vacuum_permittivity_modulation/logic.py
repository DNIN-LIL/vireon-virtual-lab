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


def _as_float(v, default: float) -> float:
    if v is None:
        return float(default)
    return float(v)


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


def run(cfg=None, medium: Medium | None = None, *args, **kwargs):
    cfg, medium = _normalize_args(cfg, medium, list(args))
    if medium is None:
        raise ValueError("medium is required")

    Q = _as_float(cfg.get("charge"), 1e-6)
    f_hz = _as_float(cfg.get("frequency_hz"), 1.0e6)
    m = _as_float(cfg.get("mass"), 1.0)
    k_const = _as_float(cfg.get("default_k"), 1.0)
    duration_s = _as_float(cfg.get("duration_s"), 1.0)
    eps_mults = _to_float_list_flexible(cfg.get("epsilon_multipliers")) or [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
    out_dir = cfg.get("output_dir", "output/vacuum_permittivity_modulation")

    _ensure_dir(out_dir)
    dt = _dt_from_sampling(cfg, medium)
    steps = max(1, int(duration_s / dt))

    base = k_const * Q * f_hz * m

    eps_mults = np.array(eps_mults, dtype=float)
    # Simple model: field/force scale inversely with permittivity multiplier
    with np.errstate(divide="ignore", invalid="ignore"):
        scale = 1.0 / eps_mults
    force = base * scale
    accel = np.divide(force, m, out=np.full_like(force, base / m), where=m != 0.0)

    data = np.column_stack([eps_mults, force, accel, scale])
    np.savetxt(
        os.path.join(out_dir, "epsilon_sweep.csv"),
        data,
        delimiter=",",
        fmt="%.6e",
        header="epsilon_multiplier,force,accel,scale"
    )

    # Plots
    fig1, ax1 = plt.subplots()
    ax1.plot(eps_mults, force, marker="o")
    ax1.set_xscale("log")
    ax1.set_xlabel("Permittivity multiplier (ε / ε0)")
    ax1.set_ylabel("Force (N)")
    ax1.set_title("Force vs Permittivity Multiplier")
    ax1.grid(True, which="both")
    fig1.tight_layout()
    fig1.savefig(os.path.join(out_dir, "force_vs_epsilon.png"))
    plt.close(fig1)

    fig2, ax2 = plt.subplots()
    ax2.plot(eps_mults, accel, marker="o")
    ax2.set_xscale("log")
    ax2.set_xlabel("Permittivity multiplier (ε / ε0)")
    ax2.set_ylabel("Acceleration (m/s²)")
    ax2.set_title("Acceleration vs Permittivity Multiplier")
    ax2.grid(True, which="both")
    fig2.tight_layout()
    fig2.savefig(os.path.join(out_dir, "accel_vs_epsilon.png"))
    plt.close(fig2)

    np.savez(
        os.path.join(out_dir, "results.npz"),
        epsilon_multipliers=eps_mults,
        force=force,
        accel=accel,
        scale=scale,
        Q=Q,
        f_hz=f_hz,
        m=m,
        k=k_const,
        dt=dt,
        steps=steps,
    )

    return {
        "steps": steps,
        "dt": dt,
        "output_dir": out_dir,
        "points": int(eps_mults.size),
        "Q": Q,
        "f_hz": f_hz,
        "k": k_const,
    }


def run_noargs():
    cfg_path = Path(__file__).resolve().parent / "config.yaml"
    cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    medium = Medium({"medium": cfg.get("medium", cfg)})
    return run(cfg, medium)
