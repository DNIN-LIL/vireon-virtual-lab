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


def _as_float(v, default: float) -> float:
    if v is None:
        return float(default)
    return float(v)


def _as_int(v, default: int) -> int:
    if v is None:
        return int(default)
    return int(v)


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


def _collision_freq(cfg: dict, medium: Medium) -> float:
    props = getattr(medium, "properties", {}) if hasattr(medium, "properties") else {}
    if isinstance(props, dict) and "collision_freq" in props and cfg.get("collision_freq") is None:
        try:
            return float(props["collision_freq"])
        except Exception:
            pass
    return _as_float(cfg.get("collision_freq"), 0.0)


def _attenuation_for_freq(f_hz: float, nu: float) -> float:
    # Collisional attenuation: 1 / sqrt(1 + (nu/omega)^2)
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
    m = _as_float(cfg.get("mass"), 1.0)
    k_const = _as_float(cfg.get("default_k"), 1.0)
    duration_s = _as_float(cfg.get("duration_s"), 1.0)
    eps_mults = _to_float_list_flexible(cfg.get("epsilon_multipliers")) or [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
    out_dir = cfg.get("output_dir", "output/vacuum_permittivity_modulation_in_plasma")

    _ensure_dir(out_dir)
    dt = _dt_from_sampling(cfg, medium)
    steps = max(1, int(duration_s / dt))

    # Plasma modifiers
    nu = _collision_freq(cfg, medium)
    scale_plasma = _plasma_scale(cfg, medium) * _attenuation_for_freq(f_hz, nu)

    # Base amplitude (vacuum)
    base = k_const * Q * f_hz * m

    eps_mults = np.array(eps_mults, dtype=float)
    # Vacuum permittivity sweep: inverse dependence on epsilon multiplier
    with np.errstate(divide="ignore", invalid="ignore"):
        scale_vac = 1.0 / eps_mults

    force = base * scale_vac * scale_plasma
    accel = np.divide(force, m, out=np.full_like(force, (base * scale_plasma) / max(m, 1e-12)), where=m != 0.0)

    # Save CSV
    np.savetxt(
        os.path.join(out_dir, "epsilon_sweep_plasma.csv"),
        np.column_stack([eps_mults, force, accel, np.full_like(force, scale_plasma), scale_vac]),
        delimiter=",",
        fmt="%.6e",
        header="epsilon_multiplier,force,accel,plasma_scale,vacuum_scale"
    )

    # Plots
    fig1, ax1 = plt.subplots()
    ax1.plot(eps_mults, force, marker="o")
    ax1.set_xscale("log")
    ax1.set_xlabel("Permittivity multiplier (ε / ε0)")
    ax1.set_ylabel("Force (N)")
    ax1.set_title("Force vs Permittivity Multiplier (plasma)")
    ax1.grid(True, which="both")
    fig1.tight_layout()
    fig1.savefig(os.path.join(out_dir, "force_vs_epsilon_plasma.png"))
    plt.close(fig1)

    fig2, ax2 = plt.subplots()
    ax2.plot(eps_mults, accel, marker="o")
    ax2.set_xscale("log")
    ax2.set_xlabel("Permittivity multiplier (ε / ε0)")
    ax2.set_ylabel("Acceleration (m/s²)")
    ax2.set_title("Acceleration vs Permittivity Multiplier (plasma)")
    ax2.grid(True, which="both")
    fig2.tight_layout()
    fig2.savefig(os.path.join(out_dir, "accel_vs_epsilon_plasma.png"))
    plt.close(fig2)

    # Summary bundle
    np.savez(
        os.path.join(out_dir, "results_plasma.npz"),
        epsilon_multipliers=eps_mults,
        force=force,
        accel=accel,
        Q=Q,
        f_hz=f_hz,
        m=m,
        k=k_const,
        plasma_scale=scale_plasma,
        nu=nu,
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
        "plasma_scale": scale_plasma,
    }


def run_noargs():
    cfg_path = Path(__file__).resolve().parent / "config.yaml"
    cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}

    # Robustly build a Medium from cfg["medium"] (string or dict)
    m_cfg = cfg.get("medium", cfg)
    if isinstance(m_cfg, str):
        m_cfg = {"type": m_cfg}
    elif isinstance(m_cfg, dict) and "type" not in m_cfg and isinstance(m_cfg.get("medium"), str):
        m_cfg = {"type": m_cfg["medium"], **{k: v for k, v in m_cfg.items() if k != "medium"}}

    medium = Medium(m_cfg)
    return run(cfg, medium)
