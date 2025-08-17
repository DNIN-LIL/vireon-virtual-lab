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


def run(cfg=None, medium: Medium | None = None, *args, **kwargs):
    cfg, medium = _normalize_args(cfg, medium, list(args))
    if medium is None:
        raise ValueError("medium is required")

    # Inputs
    R = _as_float(cfg.get("radius"), 0.2)
    N = _as_int(cfg.get("num_charges"), 100)
    omega = _as_float(cfg.get("omega_rot"), 1000.0)  # rad/s (used only for phase staggering)
    f_hz = _as_float(cfg.get("frequency_hz"), 1.0e6)
    Q = _as_float(cfg.get("charge"), 1e-6)          # per-source charge
    m = _as_float(cfg.get("mass"), 1.0)
    k_const = _as_float(cfg.get("default_k"), 1.0)
    duration_s = _as_float(cfg.get("duration_s"), 1.0)
    waveform = str(cfg.get("waveform", "all")).strip().lower()
    out_dir = cfg.get("output_dir", "output/toroidal_field_rotation")

    # Grid resolution: interpret grid_size as integer count
    grid_n = _as_int(cfg.get("grid_size"), 50)

    _ensure_dir(out_dir)
    dt = _dt_from_sampling(cfg, medium)
    steps = max(1, int(duration_s / dt))

    # Ring source positions
    idx = np.arange(N)
    theta = 2.0 * np.pi * idx / max(N, 1)
    xs = R * np.cos(theta)
    ys = R * np.sin(theta)

    # Phase per source (include a small rotation-derived spread to avoid perfect symmetry)
    phase_offset = (omega / max(f_hz, 1.0)) * (idx / max(N, 1))  # dimensionless
    phase_offset = 2.0 * np.pi * (phase_offset - np.floor(phase_offset))

    # Field amplitude per source and wavenumber
    A0 = k_const * Q * f_hz * m
    k_w = 2.0 * math.pi * f_hz / 3.0e8  # effective phase speed ~ c

    # Grid (2D plane)
    x = np.linspace(-2.0 * R, 2.0 * R, grid_n)
    y = np.linspace(-2.0 * R, 2.0 * R, grid_n)
    X, Y = np.meshgrid(x, y, indexing="xy")

    modes = ["sine", "square", "triangle", "sawtooth"] if waveform == "all" else [waveform]
    results = []

    for mode in modes:
        field = np.zeros_like(X, dtype=float)
        # Sum contributions from each source as a radial phase from its position
        for xi, yi, ph in zip(xs, ys, phase_offset):
            r = np.hypot(X - xi, Y - yi)
            field += A0 * _drive(mode, k_w * r + ph)

        potential = -field

        # Save CSVs
        np.savetxt(os.path.join(out_dir, f"field_{mode}.csv"), field, delimiter=",", fmt="%.6e")
        np.savetxt(os.path.join(out_dir, f"potential_{mode}.csv"), potential, delimiter=",", fmt="%.6e")

        # Heatmap
        fig1, ax1 = plt.subplots()
        im1 = ax1.imshow(field, origin="lower", aspect="auto",
                         extent=[x.min(), x.max(), y.min(), y.max()])
        ax1.set_title(f"Toroidal Field (mode={mode})")
        ax1.set_xlabel("x")
        ax1.set_ylabel("y")
        fig1.colorbar(im1, ax=ax1)
        fig1.tight_layout()
        fig1.savefig(os.path.join(out_dir, f"field_{mode}.png"))
        plt.close(fig1)

        # Quiver of gradient (warning-safe)
        dy = y[1] - y[0] if len(y) > 1 else 1.0
        dx = x[1] - x[0] if len(x) > 1 else 1.0
        dFy, dFx = np.gradient(field, dy, dx)

        step = max(1, grid_n // 25)
        Xs = X[::step, ::step]; Ys = Y[::step, ::step]
        Us = dFx[::step, ::step]; Vs = dFy[::step, ::step]

        mag = np.hypot(Us, Vs)
        thr = max(float(np.nanmax(mag)), 1.0) * 1e-12
        mask = mag > thr

        fig2, ax2 = plt.subplots()
        if np.any(mask):
            ax2.quiver(
                Xs[mask], Ys[mask], Us[mask], Vs[mask],
                angles="xy", scale_units="xy", scale=1.0, width=0.003
            )
        else:
            ax2.text(0.5, 0.5, "All-zero vector field",
                     ha="center", va="center", transform=ax2.transAxes)

        ax2.set_title(f"Field Gradient (quiver) — {mode}")
        ax2.set_xlabel("x")
        ax2.set_ylabel("y")
        fig2.tight_layout()
        fig2.savefig(os.path.join(out_dir, f"field_grad_{mode}.png"))
        plt.close(fig2)

        results.append(mode)

    # Summaries
    np.savez(
        os.path.join(out_dir, "summary.npz"),
        modes=np.array(results, dtype=object),
        grid_n=grid_n,
        radius=R,
        num_charges=N,
        omega_rot=omega,
        A0=A0,
        k_w=k_w,
        dt=dt,
        steps=steps,
        ring_x=xs,
        ring_y=ys,
    )

    return {
        "modes": results,
        "dt": dt,
        "steps": steps,
        "grid_n": grid_n,
        "num_charges": N,
        "radius": R,
        "output_dir": out_dir,
    }


def run_noargs():
    cfg_path = Path(__file__).resolve().parent / "config.yaml"
    cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    medium = Medium({"medium": cfg.get("medium", cfg)})
    return run(cfg, medium)
