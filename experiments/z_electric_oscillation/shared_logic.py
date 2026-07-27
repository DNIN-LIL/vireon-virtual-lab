import os
from pathlib import Path
import math
import numpy as np

from core.config_loader import load_config
from core.medium import Medium


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def as_float(v, default: float) -> float:
    return float(default) if v is None else float(v)


def as_int(v, default: int) -> int:
    return int(default) if v is None else int(v)


def dt_from_sampling(cfg: dict, medium: Medium) -> float:
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


def load_config_if_needed(cfg):
    if isinstance(cfg, dict) or cfg is None:
        return cfg or {}
    p = Path(str(cfg))
    if p.suffix.lower() in (".yml", ".yaml") and p.exists():
        return load_config(str(p))
    return {}


def normalize_args(cfg, medium, args):
    if isinstance(cfg, str):
        if args:
            cfg, medium = args[0], (args[1] if len(args) > 1 else medium)
        else:
            cfg_path = Path(__file__).resolve().parent / "config.yaml"
            cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    cfg = load_config_if_needed(cfg)
    return cfg, medium


def drive(kind: str, x: np.ndarray) -> np.ndarray:
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


def _child_name_from_cfg(cfg: dict) -> str:
    if cfg.get("__child_name__"):
        return str(cfg["__child_name__"])
    if cfg.get("__exp_name__"):
        return str(cfg["__exp_name__"])
    od = cfg.get("output_dir")
    if od:
        try:
            return Path(str(od)).name or "subexp"
        except Exception:
            pass
    return "subexp"


def _waveform_from_child(child_name: str, default: str = "sine") -> str:
    name = child_name.lower()
    for w in ("sine", "square", "triangle", "sawtooth"):
        if name.endswith(w):
            return w
    return default


def _plasma_scale(f_hz: float, medium: Medium, cfg: dict) -> float:
    mtype = str(getattr(medium, "type", "vacuum")).lower()
    if mtype != "plasma":
        return 1.0

    props = getattr(medium, "properties", {}) if hasattr(medium, "properties") else {}
    scale = 1.0

    sf = props.get("screening_factor")
    if sf is not None:
        try:
            scale *= float(sf)
        except Exception:
            pass
    elif "relative_permittivity" in props:
        try:
            eps_r = float(props["relative_permittivity"])
            if eps_r > 0:
                scale *= eps_r
        except Exception:
            pass

    nu = None
    if isinstance(props, dict) and "collision_freq" in props:
        try:
            nu = float(props["collision_freq"])
        except Exception:
            nu = None
    if nu is None:
        try:
            nu = float(cfg.get("collision_freq", 0.0))
        except Exception:
            nu = 0.0

    try:
        omega = 2.0 * math.pi * float(f_hz)
        if omega > 0.0 and nu and nu > 0.0:
            scale *= 1.0 / math.sqrt(1.0 + (nu / omega) ** 2)
    except Exception:
        pass

    return float(scale)


def _has_key(c: dict, k: str) -> bool:
    if k not in c:
        return False
    v = c.get(k)
    if v is None:
        return False
    if isinstance(v, str) and v.strip() == "":
        return False
    return True


def run_electric(cfg=None, medium: Medium | None = None, *args, **kwargs):
    cfg, medium = normalize_args(cfg, medium, list(args))
    if medium is None:
        raise ValueError("medium is required")

    # Electric requires 'charge' and forbids 'magnetic_charge'
    if _has_key(cfg, "magnetic_charge"):
        raise ValueError("Invalid parameter for electric oscillation: 'magnetic_charge' detected. Use 'charge'.")
    if not _has_key(cfg, "charge"):
        raise ValueError("Missing required parameter 'charge' for electric oscillation.")

    child_name = _child_name_from_cfg(cfg)
    mode = str(cfg.get("waveform", _waveform_from_child(child_name))).strip().lower()
    if mode == "all":
        mode = _waveform_from_child(child_name, "sine")

    Q = as_float(cfg.get("charge"), 1e-6)
    f_hz = as_float(cfg.get("frequency_hz"), 1.0e6)
    m = as_float(cfg.get("mass"), 1.0)
    k_const = as_float(cfg.get("default_k"), 1.0)
    duration_s = as_float(cfg.get("duration_s"), 1.0)

    default_out = Path("output") / "z_electric_oscillation" / child_name
    out_dir = Path(cfg.get("output_dir", default_out))
    ensure_dir(str(out_dir))

    dt = dt_from_sampling(cfg, medium)
    steps = max(1, int(duration_s / dt))
    t = np.arange(steps, dtype=float) * dt

    A0 = k_const * Q * f_hz * m
    A = A0 * _plasma_scale(f_hz, medium, cfg)
    w = 2.0 * math.pi * f_hz
    phi = w * t

    # Clockwise: Ey lags Ex by 90 degrees
    Ex = A * drive(mode, phi)
    Ey = A * drive(mode, phi - 0.5 * math.pi)

    # Legacy scalar output (Ey)
    y = Ey

    peak = float(np.max(np.abs(y))) if y.size else 0.0
    rms = float(np.sqrt(np.mean(y * y))) if y.size else 0.0
    mean = float(np.mean(y)) if y.size else 0.0
    crest = (peak / rms) if rms > 0 else float("inf")
    direction = "clockwise"

    np.savetxt(
        out_dir / "time_series.csv",
        np.column_stack([t, y]),
        delimiter=",",
        fmt="%.6e",
        header="t,y"
    )
    np.savetxt(
        out_dir / "vector_time_series.csv",
        np.column_stack([t, Ex, Ey]),
        delimiter=",",
        fmt="%.6e",
        header="t,Ex,Ey"
    )

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    max_pts = 5000
    if t.size > max_pts:
        ax.plot(t[:max_pts], y[:max_pts], label=f"{mode} ({direction})")
    else:
        ax.plot(t, y, label=f"{mode} ({direction})")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Ey")
    ax.set_title(f"{child_name} — {mode} ({direction})")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_dir / "signal.png")
    plt.close(fig)

    fig2, ax2 = plt.subplots()
    n = min(t.size, 4000)
    ax2.plot(Ex[:n], Ey[:n])
    ax2.set_aspect("equal", adjustable="box")
    ax2.set_xlabel("Ex")
    ax2.set_ylabel("Ey")
    ax2.set_title(f"Orbit — {child_name} ({direction})")
    ax2.grid(True)
    fig2.tight_layout()
    fig2.savefig(out_dir / "orbit.png")
    plt.close(fig2)

    return {
        "child": child_name,
        "waveform": mode,
        "direction": direction,
        "dt": dt,
        "steps": steps,
        "A0": A0,
        "A": A,
        "output_dir": str(out_dir),
    }
