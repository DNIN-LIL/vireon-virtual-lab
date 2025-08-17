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


def _to_str_list(val):
    if val is None:
        return []
    if isinstance(val, (list, tuple)):
        items = [str(x).strip().lower() for x in val]
    else:
        items = [s.strip().lower() for s in str(val).split(",")]
    return [s for s in items if s]


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
        # heuristic boost if user didn’t override
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

    Q = _as_float(cfg.get("charge"), 1e-6)
    f_hz = _as_float(cfg.get("frequency_hz"), 1.0e6)
    m = _as_float(cfg.get("mass"), 1.0)
    k_const = _as_float(cfg.get("default_k"), 1.0)
    duration_s = _as_float(cfg.get("duration_s"), 1.0)
    out_dir = cfg.get("output_dir", "output/waveform_shape_response_in_plasma")

    waves = _to_str_list(cfg.get("waveforms")) or ["sine", "square", "triangle"]
    if "all" in waves:
        waves = ["sine", "square", "triangle", "sawtooth"]

    _ensure_dir(out_dir)

    dt = _dt_from_sampling(cfg, medium)
    steps = max(1, int(duration_s / dt))
    t = np.arange(steps, dtype=float) * dt
    w = 2.0 * math.pi * f_hz

    # Plasma scaling
    nu = _collision_freq(cfg, medium)
    scale_plasma = _plasma_scale(cfg, medium) * _attenuation_for_freq(f_hz, nu)

    # Amplitude
    A = k_const * Q * f_hz * m * scale_plasma

    metrics = []
    overlay = []

    for mode in waves:
        y = A * _drive(mode, w * t)

        peak = float(np.max(np.abs(y))) if y.size else 0.0
        rms = float(np.sqrt(np.mean(y * y))) if y.size else 0.0
        mean = float(np.mean(y)) if y.size else 0.0
        crest = (peak / rms) if rms > 0 else np.inf

        np.savetxt(
            os.path.join(out_dir, f"time_series_{mode}.csv"),
            np.column_stack([t, y]),
            delimiter=",",
            fmt="%.6e",
            header="t,y"
        )

        metrics.append((mode, peak, rms, crest, mean))
        overlay.append((mode, t, y))

    if metrics:
        arr = np.array(metrics, dtype=object)
        np.savetxt(
            os.path.join(out_dir, "summary_metrics.csv"),
            np.column_stack([arr[:, 0],
                             arr[:, 1].astype(float),
                             arr[:, 2].astype(float),
                             arr[:, 3].astype(float),
                             arr[:, 4].astype(float)]),
            delimiter=",",
            fmt="%s",
            header="waveform,peak,rms,crest_factor,mean"
        )

    fig, ax = plt.subplots()
    max_plot_points = 5000
    for mode, tt, yy in overlay:
        if tt.size > max_plot_points:
            cut = max_plot_points
            ax.plot(tt[:cut], yy[:cut], label=mode)
        else:
            ax.plot(tt, yy, label=mode)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Response")
    ax.set_title("Waveform Shape Response (plasma, overlay)")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, "waveform_overlay_plasma.png"))
    plt.close(fig)

    np.savez(
        os.path.join(out_dir, "results_plasma.npz"),
        time=t,
        waves=np.array([w for w, *_ in overlay], dtype=object),
        Q=Q, f_hz=f_hz, m=m, k=k_const,
        A=A, dt=dt, steps=steps,
        plasma_scale=scale_plasma, nu=nu
    )

    return {
        "dt": dt,
        "steps": steps,
        "output_dir": out_dir,
        "waves": waves,
        "A": A,
        "plasma_scale": scale_plasma,
    }


def run_noargs():
    cfg_path = Path(__file__).resolve().parent / "config.yaml"
    cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    medium = Medium({"medium": cfg.get("medium", cfg)})
    return run(cfg, medium)
