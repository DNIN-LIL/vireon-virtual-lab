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


def _drive(kind: str, x):
    if kind == "sine":
        return np.sin(x)
    if kind == "square":
        return np.sign(np.sin(x))
    if kind == "triangle":
        return 2.0 / np.pi * np.arcsin(np.sin(x))
    if kind == "sawtooth":
        frac = (x / (2.0 * np.pi)) % 1.0
        return 2.0 * (frac - 0.5)
    return np.sin(x)


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
    omega = 2.0 * math.pi * float(f_hz)
    if omega <= 0.0:
        return 1.0
    return 1.0 / math.sqrt(1.0 + (nu / omega) ** 2)


def run(cfg=None, medium: Medium | None = None, *args, **kwargs):
    cfg, medium = _normalize_args(cfg, medium, list(args))
    if medium is None:
        raise ValueError("medium is required")

    f_hz = _as_float(cfg.get("frequency_hz"), 1.0e6)
    Q = _as_float(cfg.get("charge"), 1e-9)
    m = _as_float(cfg.get("mass"), 1e-6)
    k_const = _as_float(cfg.get("default_k"), 1.0)
    duration_s = _as_float(cfg.get("duration_s"), 1.0)
    wave_speed = _as_float(cfg.get("wave_speed"), 3.0e8)
    out_dir = cfg.get("output_dir", "output/resonant_particle_field_in_plasma")
    waveform = str(cfg.get("waveform", "all")).strip().lower()
    grid_n = _as_int(cfg.get("grid_size"), 50)

    _ensure_dir(out_dir)
    dt = _dt_from_sampling(cfg, medium)
    steps = max(1, int(duration_s / dt))

    x = np.linspace(-1.0, 1.0, grid_n)
    y = np.linspace(-1.0, 1.0, grid_n)
    X, Y = np.meshgrid(x, y, indexing="xy")
    R = np.sqrt(X * X + Y * Y)

    # Plasma scaling
    nu = _collision_freq(cfg, medium)
    scale = _plasma_scale(cfg, medium) * _attenuation_for_freq(f_hz, nu)

    # Amplitude and wave number
    A = k_const * Q * f_hz * m * scale
    k_w = 2.0 * math.pi * f_hz / max(wave_speed, 1.0)
    phase = k_w * R

    modes = ["sine", "square", "triangle", "sawtooth"] if waveform == "all" else [waveform]
    outputs = []

    for mode in modes:
        field = A * _drive(mode, phase)
        potential = -field

        np.savetxt(os.path.join(out_dir, f"field_{mode}.csv"), field, delimiter=",", fmt="%.6e")
        np.savetxt(os.path.join(out_dir, f"potential_{mode}.csv"), potential, delimiter=",", fmt="%.6e")

        fig1, ax1 = plt.subplots()
        im1 = ax1.imshow(field, origin="lower", aspect="auto")
        ax1.set_title(f"Resonant Particle Field (plasma) — {mode}")
        ax1.set_xlabel("x index")
        ax1.set_ylabel("y index")
        fig1.colorbar(im1, ax=ax1)
        fig1.tight_layout()
        fig1.savefig(os.path.join(out_dir, f"field_{mode}.png"))
        plt.close(fig1)

        dy = y[1] - y[0] if len(y) > 1 else 1.0
        dx = x[1] - x[0] if len(x) > 1 else 1.0
        dFy, dFx = np.gradient(field, dy, dx)
        step = max(1, grid_n // 25)
        fig2, ax2 = plt.subplots()
        ax2.quiver(
            X[::step, ::step], Y[::step, ::step],
            dFx[::step, ::step], dFy[::step, ::step],
            scale=None
        )
        ax2.set_title(f"Field Gradient (quiver) — {mode}")
        ax2.set_xlabel("x")
        ax2.set_ylabel("y")
        fig2.tight_layout()
        fig2.savefig(os.path.join(out_dir, f"field_grad_{mode}.png"))
        plt.close(fig2)

        outputs.append(mode)

    np.savez(
        os.path.join(out_dir, "summary.npz"),
        modes=np.array(outputs, dtype=object),
        grid_n=grid_n,
        A=A,
        k_w=k_w,
        dt=dt,
        steps=steps,
        scale=scale,
        nu=nu,
    )

    return {
        "modes": outputs,
        "dt": dt,
        "steps": steps,
        "grid_n": grid_n,
        "output_dir": out_dir,
        "plasma_scale": scale,
    }


def run_noargs():
    cfg_path = Path(__file__).resolve().parent / "config.yaml"
    cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    medium = Medium({"medium": cfg.get("medium", cfg)})
    return run(cfg, medium)
