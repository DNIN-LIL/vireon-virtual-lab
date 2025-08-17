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
    sr_raw = cfg.get("sampling_rate", 0.0)
    sr = float(sr_raw)
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
    # Accept: (cfg, medium), ("exp_name", cfg, medium), (cfg_path, medium), (cfg), ()
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


def run(cfg=None, medium: Medium | None = None, *args, **kwargs):
    cfg, medium = _normalize_args(cfg, medium, list(args))
    if medium is None:
        raise ValueError("medium is required")

    # Accept lists or single scalars (with defaults if neither provided)
    charges = _get_list(cfg, "charges", "charge", [1e-9])
    freqs_hz = _get_list(cfg, "frequencies", "frequency", [1.0e6])
    angles_deg = _get_list(cfg, "orientation_angles_deg", "angle", [0, 15, 30, 45, 60, 75, 90])

    mass = _as_float(cfg.get("mass"), 1.0)
    k = _as_float(cfg.get("default_k"), 1.0)
    field_strength = _as_float(cfg.get("field_strength"), 1.0)
    duration_s = _as_float(cfg.get("duration_s"), 1.0)
    out_dir = cfg.get("output_dir", "output/field_orientation_variance_in_plasma")

    _ensure_dir(out_dir)
    dt = _dt_from_sampling(cfg, medium)
    steps = max(1, int(duration_s / dt))

    scale_factor = _plasma_scale(cfg, medium)

    forces = np.zeros((len(angles_deg), len(charges), len(freqs_hz)), dtype=float)
    freq_labels = [float(f) for f in freqs_hz]
    charge_labels = [float(q) for q in charges]

    for ai, deg in enumerate(angles_deg):
        proj = abs(np.cos(np.deg2rad(float(deg))))
        for i, Q in enumerate(charges):
            Qi = float(Q)
            for j, f_hz in enumerate(freqs_hz):
                forces[ai, i, j] = k * Qi * float(f_hz) * mass * field_strength * proj * scale_factor

        tag = int(round(float(deg)))
        np.savetxt(
            os.path.join(out_dir, f"force_matrix_angle_{tag}deg.csv"),
            forces[ai],
            delimiter=",",
            fmt="%.6e",
        )

        fig, ax = plt.subplots()
        im = ax.imshow(forces[ai], cmap="plasma", origin="lower", aspect="auto")
        ax.set_xticks(np.arange(len(freq_labels)))
        ax.set_yticks(np.arange(len(charge_labels)))
        ax.set_xticklabels([f"{f:.0e}" for f in freq_labels])
        ax.set_yticklabels([f"{q:.0e}" for q in charge_labels])
        ax.set_xlabel("Frequency (Hz)")
        ax.set_ylabel("Charge (C)")
        ax.set_title(f"Plasma-Modified Force (N) at {deg}°")
        fig.colorbar(im, ax=ax)
        fig.tight_layout()
        fig.savefig(os.path.join(out_dir, f"force_matrix_angle_{tag}deg.png"))
        plt.close(fig)

    np.savez(
        os.path.join(out_dir, "forces_3d.npz"),
        forces=forces,
        charges=np.array(charge_labels),
        frequencies=np.array(freq_labels),
        angles=np.array([float(a) for a in angles_deg]),
        plasma_scale=scale_factor,
    )

    return {
        "steps": steps,
        "dt": dt,
        "output_dir": out_dir,
        "shape": forces.shape,
        "plasma_scale": scale_factor,
    }


def run_noargs():
    cfg_path = Path(__file__).resolve().parent / "config.yaml"
    cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    medium = Medium({"medium": cfg.get("medium", cfg)})
    return run(cfg, medium)
