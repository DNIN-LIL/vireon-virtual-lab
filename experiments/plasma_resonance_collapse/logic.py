import os
import math
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from core.medium import Medium
from core.config_loader import load_config


def _ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


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
    # Prefer cfg override, else medium.properties.collision_freq
    props = getattr(medium, "properties", {}) if hasattr(medium, "properties") else {}
    if isinstance(props, dict) and "collision_freq" in props and cfg.get("collision_freq") is None:
        try:
            return float(props["collision_freq"])
        except Exception:
            pass
    return _as_float(cfg.get("collision_freq"), 0.0)


def _attenuation_for_freq(f_hz: float, nu: float) -> float:
    # 1 / sqrt(1 + (nu/omega)^2)
    omega = 2.0 * math.pi * float(f_hz)
    if omega <= 0.0:
        return 1.0
    return 1.0 / math.sqrt(1.0 + (nu / omega) ** 2)


def _drive(kind: str, t: np.ndarray, f_hz: float) -> np.ndarray:
    w = 2.0 * math.pi * float(f_hz)
    if kind == "sine":
        return np.sin(w * t)
    if kind == "square":
        return np.sign(np.sin(w * t))
    if kind == "triangle":
        # scaled saw mirrored
        return 2.0 / math.pi * np.arcsin(np.sin(w * t))
    if kind == "sawtooth":
        # range [-1,1]
        frac = (t * f_hz) % 1.0
        return 2.0 * (frac - 0.5)
    return np.sin(w * t)


def _run_single_mode(cfg: dict, medium: Medium, mode: str):
    particles = _as_int(cfg.get("particles"), 500)
    r0 = _as_float(cfg.get("radius"), 1.0)
    f_hz = _as_float(cfg.get("frequency"), 5.0e5)
    Q = _as_float(cfg.get("charge"), 1e-9)
    m = _as_float(cfg.get("mass"), 1e-6)
    k_const = _as_float(cfg.get("default_k"), 1.0)
    steps_cfg = cfg.get("steps")
    steps = _as_int(steps_cfg, 1000)
    theta0 = math.radians(_as_float(cfg.get("theta"), 0.0))
    out_dir = cfg.get("output_dir", "output/plasma_resonance_collapse")

    _ensure_dir(out_dir)
    dt = _dt_from_sampling(cfg, medium)

    nu = _collision_freq(cfg, medium)
    gamma = _as_float(cfg.get("magnetic_drag_coeff"), 0.0) + nu
    scale = _plasma_scale(cfg, medium) * _attenuation_for_freq(f_hz, nu)

    F0 = k_const * Q * f_hz * m * scale

    t = np.arange(steps) * dt
    drive = _drive(mode, t, f_hz)

    rng = np.random.default_rng(42)
    angles = theta0 + rng.uniform(0, 2 * math.pi, size=particles)
    r = np.full(particles, r0, dtype=float) + rng.normal(0.0, 0.01 * r0, size=particles)
    vr = np.zeros_like(r)

    mean_r = np.empty(steps, dtype=float)
    min_r = np.empty(steps, dtype=float)
    max_r = np.empty(steps, dtype=float)

    for k in range(steps):
        a = (F0 * drive[k]) / m - gamma * vr
        vr = vr + a * dt
        r = r + vr * dt
        mean_r[k] = float(np.mean(r))
        min_r[k] = float(np.min(r))
        max_r[k] = float(np.max(r))

    collapse_idx = int(np.argmax(mean_r <= 0.9 * r0)) if np.any(mean_r <= 0.9 * r0) else -1

    tag = mode
    np.savetxt(os.path.join(out_dir, f"time_series_{tag}.csv"),
               np.column_stack([t, mean_r, min_r, max_r]),
               delimiter=",", fmt="%.6e", header="t,mean_r,min_r,max_r")

    fig1, ax1 = plt.subplots()
    ax1.plot(t, mean_r, label="mean r")
    ax1.plot(t, min_r, label="min r", alpha=0.7)
    ax1.plot(t, max_r, label="max r", alpha=0.7)
    if collapse_idx >= 0:
        ax1.axvline(t[collapse_idx], linestyle="--", alpha=0.6)
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Radius")
    ax1.set_title(f"Resonance Collapse — {mode}")
    ax1.grid(True)
    ax1.legend()
    fig1.tight_layout()
    fig1.savefig(os.path.join(out_dir, f"radius_timeseries_{tag}.png"))
    plt.close(fig1)

    fig2, ax2 = plt.subplots(subplot_kw={"projection": "polar"})
    ax2.scatter(angles, r, s=6, alpha=0.6)
    ax2.set_title(f"Final Particle Radii — {mode}")
    fig2.tight_layout()
    fig2.savefig(os.path.join(out_dir, f"final_polar_{tag}.png"))
    plt.close(fig2)

    np.savez(
        os.path.join(out_dir, f"results_{tag}.npz"),
        t=t, mean_r=mean_r, min_r=min_r, max_r=max_r,
        r_final=r, angles=angles,
        collapse_idx=collapse_idx, r0=r0,
        params=dict(F0=F0, Q=Q, f_hz=f_hz, m=m, k=k_const, dt=dt, steps=steps,
                    gamma=gamma, scale=scale)
    )

    return {
        "mode": mode,
        "dt": dt,
        "steps": steps,
        "collapse_index": collapse_idx,
        "collapse_time": (float(t[collapse_idx]) if collapse_idx >= 0 else None),
        "output_dir": out_dir,
    }


def run(cfg=None, medium: Medium | None = None, *args, **kwargs):
    cfg, medium = _normalize_args(cfg, medium, list(args))
    if medium is None:
        raise ValueError("medium is required")

    waveform = str(cfg.get("waveform", "sine")).strip().lower()
    modes = ["sine", "square", "triangle", "sawtooth"] if waveform == "all" else [waveform]

    results = []
    for mode in modes:
        results.append(_run_single_mode(cfg, medium, mode))

    # Return a compact summary; detailed artifacts are written to disk.
    return {
        "modes": [r["mode"] for r in results],
        "dt": results[0]["dt"],
        "steps": results[0]["steps"],
        "collapse_times": [r["collapse_time"] for r in results],
        "output_dir": results[0]["output_dir"],
    }


def run_noargs():
    cfg_path = Path(__file__).resolve().parent / "config.yaml"
    cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    medium = Medium({"medium": cfg.get("medium", cfg)})
    return run(cfg, medium)
