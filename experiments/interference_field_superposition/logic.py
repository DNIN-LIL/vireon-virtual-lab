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


def _as_int(val, default: int) -> int:
    if val is None:
        return int(default)
    return int(val)


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
    # Accept: (cfg, medium), ("exp_name", cfg, medium), (cfg_path, medium), (cfg), ()
    if isinstance(cfg, str):
        if args:
            cfg, medium = args[0], (args[1] if len(args) > 1 else medium)
        else:
            cfg_path = Path(__file__).resolve().parent / "config.yaml"
            cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    cfg = _load_cfg_if_needed(cfg)
    return cfg, medium


def _tile_to_length(lst, n):
    if len(lst) == n:
        return lst
    if len(lst) == 1:
        return [lst[0]] * n
    reps = math.ceil(n / len(lst))
    out = (lst * reps)[:n]
    return out


def _unit_dirs(mode: str, n: int, spin_direction: str):
    # Returns n unit vectors in the plane
    dirs = []
    sgn = -1.0 if str(spin_direction).lower().startswith("counter") else 1.0
    if str(mode).lower() == "random":
        rng = np.random.default_rng(12345)
        angles = rng.uniform(0, 2 * np.pi, size=n)
    else:
        # evenly spaced
        angles = np.linspace(0.0, 2 * np.pi, num=n, endpoint=False)
    for a in angles:
        a = sgn * a
        dirs.append((math.cos(a), math.sin(a)))
    return dirs


def run(cfg=None, medium: Medium | None = None, *args, **kwargs):
    cfg, medium = _normalize_args(cfg, medium, list(args))
    if medium is None:
        raise ValueError("medium is required")

    # Inputs (accept lists or single scalars; defaults mirror your config prompts)
    charges = _get_list(cfg, "charges", "charge", [1e-3, 1e-3, 1e-3])
    freqs_hz = _get_list(cfg, "frequencies", "frequency", [1.0e6, 1.0e6, 1.0e6])
    phases_deg = _get_list(cfg, "phase_offsets", "phase_offset", [0.0, 120.0, 240.0])

    n_sources = max(len(charges), len(freqs_hz), len(phases_deg))
    charges = _tile_to_length(charges, n_sources)
    freqs_hz = _tile_to_length(freqs_hz, n_sources)
    phases_deg = _tile_to_length(phases_deg, n_sources)

    mass = _as_float(cfg.get("mass"), 1.0)
    k_const = _as_float(cfg.get("default_k"), 1.0)
    duration_s = _as_float(cfg.get("duration_s"), 1.0)
    wave_speed = _as_float(cfg.get("wave_speed"), 3.0e8)  # effective phase speed
    spin_direction = str(cfg.get("spin_direction", "clockwise"))

    grid_points = _as_int(cfg.get("grid_points"), 50)
    # grid_size can be scalar, "x,y(,z)", or list
    gsize = _to_float_list_flexible(cfg.get("grid_size"))
    if not gsize:
        gsize = [1.0, 1.0, 1.0]
    if len(gsize) == 1:
        gsize = [gsize[0], gsize[0], gsize[0]]
    Lx, Ly = float(gsize[0]), float(gsize[1])

    out_dir = cfg.get("output_dir", "output/interference_field_superposition")
    _ensure_dir(out_dir)

    # Time bookkeeping (not integrating here, but preserved for consistency)
    dt = _dt_from_sampling(cfg, medium)
    steps = max(1, int(duration_s / dt))

    # Build plane-wave directions
    dirs = _unit_dirs(str(cfg.get("mode", "random")), n_sources, spin_direction)

    # Amplitudes and wave numbers
    amps = [k_const * float(Q) * float(f) * mass for Q, f in zip(charges, freqs_hz)]
    ks = [2.0 * math.pi * float(f) / wave_speed for f in freqs_hz]
    phases = [math.radians(float(p)) for p in phases_deg]

    # Grid
    x = np.linspace(0.0, Lx, grid_points)
    y = np.linspace(0.0, Ly, grid_points)
    X, Y = np.meshgrid(x, y, indexing="xy")

    # Interference field (static snapshot)
    field = np.zeros_like(X, dtype=float)
    for (ux, uy), A, k_w, phi in zip(dirs, amps, ks, phases):
        field += A * np.cos(k_w * (ux * X + uy * Y) + phi)

    # Potential (simple surrogate: V = -field)
    potential = -field

    # Vector field via spatial gradient
    dy = y[1] - y[0] if len(y) > 1 else 1.0
    dx = x[1] - x[0] if len(x) > 1 else 1.0
    dFy, dFx = np.gradient(field, dy, dx)  # note order (rows=y, cols=x)
    Fx = dFx
    Fy = dFy

    # Gravimeter signal along vertical centerline
    gsig = field[:, grid_points // 2]

    # Save CSVs
    np.savetxt(os.path.join(out_dir, "force_map.csv"), field, delimiter=",", fmt="%.6e")
    np.savetxt(os.path.join(out_dir, "potential_map.csv"), potential, delimiter=",", fmt="%.6e")
    np.savetxt(os.path.join(out_dir, "force_vector_x.csv"), Fx, delimiter=",", fmt="%.6e")
    np.savetxt(os.path.join(out_dir, "force_vector_y.csv"), Fy, delimiter=",", fmt="%.6e")
    np.savetxt(os.path.join(out_dir, "gravimeter_signal.csv"), gsig, delimiter=",", fmt="%.6e")

    # Phasor summary for debugging
    ph = np.column_stack([
        np.array(amps, dtype=float),
        np.array(freqs_hz, dtype=float),
        np.array(phases_deg, dtype=float),
        np.array([d[0] for d in dirs], dtype=float),
        np.array([d[1] for d in dirs], dtype=float),
        np.array(ks, dtype=float),
    ])
    np.savetxt(
        os.path.join(out_dir, "phasor_summary.csv"),
        ph,
        delimiter=",",
        fmt="%.6e",
        header="amplitude,frequency_hz,phase_deg,ux,uy,k_wave"
    )

    # Plots
    fig1, ax1 = plt.subplots()
    im1 = ax1.imshow(field, origin="lower", aspect="auto")
    ax1.set_title("Interference Force Map")
    ax1.set_xlabel("x index")
    ax1.set_ylabel("y index")
    fig1.colorbar(im1, ax=ax1)
    fig1.tight_layout()
    fig1.savefig(os.path.join(out_dir, "force_map.png"))
    plt.close(fig1)

    fig2, ax2 = plt.subplots()
    im2 = ax2.imshow(potential, origin="lower", aspect="auto")
    ax2.set_title("Potential Map (surrogate)")
    ax2.set_xlabel("x index")
    ax2.set_ylabel("y index")
    fig2.colorbar(im2, ax=ax2)
    fig2.tight_layout()
    fig2.savefig(os.path.join(out_dir, "potential_map.png"))
    plt.close(fig2)

    # Quiver (downsample for readability)
    step = max(1, grid_points // 25)
    fig3, ax3 = plt.subplots()
    ax3.quiver(
        X[::step, ::step], Y[::step, ::step],
        Fx[::step, ::step], Fy[::step, ::step],
        scale=None
    )
    ax3.set_title("Force Vector Field (quiver)")
    ax3.set_xlabel("x")
    ax3.set_ylabel("y")
    fig3.tight_layout()
    fig3.savefig(os.path.join(out_dir, "force_vector_quiver.png"))
    plt.close(fig3)

    return {
        "steps": steps,
        "dt": dt,
        "output_dir": out_dir,
        "grid_points": grid_points,
        "sources": n_sources,
    }


def run_noargs():
    cfg_path = Path(__file__).resolve().parent / "config.yaml"
    cfg = load_config(str(cfg_path)) if cfg_path.exists() else {}
    medium = Medium({"medium": cfg.get("medium", cfg)})
    return run(cfg, medium)
