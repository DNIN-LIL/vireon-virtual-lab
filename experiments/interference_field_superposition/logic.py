import os
import math
import numpy as np
import matplotlib.pyplot as plt
from core.medium import Medium
from core.waveform_generator import sine, square, triangle
from core.physics import compute_force
from core.visualizer import save_plot

def _ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def _wave_func(name: str):
    n = (name or "sine").lower()
    if n == "sine":
        return sine
    if n == "square":
        return square
    if n == "triangle":
        return triangle
    return sine

def _domain_from_cfg(cfg: dict):
    gs = cfg.get("grid_size", [1.0, 1.0, 1.0])
    if isinstance(gs, (int, float)):
        Lx = Ly = float(gs)
    else:
        Lx = float(gs[0])
        Ly = float(gs[1])
    n = int(cfg.get("grid_points", 50))
    x = np.linspace(-0.5 * Lx, 0.5 * Lx, n)
    y = np.linspace(-0.5 * Ly, 0.5 * Ly, n)
    X, Y = np.meshgrid(x, y, indexing="xy")
    return X, Y

def _dt(cfg: dict, medium: Medium) -> float:
    sr = float(cfg.get("sampling_rate", 0)) or 0.0
    return (1.0 / sr) if sr > 0.0 else float(medium.dt)

def _source_positions(Lx: float, Ly: float):
    # three in-line sources centered along x-axis, z=0 plane
    a = 0.25 * Lx
    return np.array([[-a, 0.0, 0.0], [0.0, 0.0, 0.0], [a, 0.0, 0.0]], dtype=float)

def run(cfg: dict, medium: Medium):
    out_dir = cfg.get("output_dir", "output/interference_field_superposition")
    _ensure_dir(out_dir)

    charges = [float(x) for x in cfg.get("charges", [0.001, 0.001, 0.001])]
    freqs_hz = [float(x) for x in cfg.get("frequencies", [1e6, 1e6, 1e6])]
    phases_deg = [float(x) for x in cfg.get("phase_offsets", [0.0, 120.0, 240.0])]
    mass = float(cfg.get("mass", 1.0))
    k = float(cfg.get("default_k", 1.0))
    wave = _wave_func(cfg.get("waveform", "sine"))

    # grid/domain
    X, Y = _domain_from_cfg(cfg)
    Lx = X.max() - X.min()
    Ly = Y.max() - Y.min()
    sources = _source_positions(Lx, Ly)
    n = X.shape[0]

    # time snapshot (mid-run)
    duration_s = float(cfg.get("duration_s", 1.0))
    t = 0.5 * duration_s
    dt = _dt(cfg, medium)  # kept for parity/consistency

    Fx = np.zeros_like(X, dtype=float)
    Fy = np.zeros_like(Y, dtype=float)

    # compute net force at each grid cell in z=0 plane
    for sx, sy, sz in sources:
        for Q, f_hz, ph_deg in zip(charges, freqs_hz, phases_deg):
            # time shift for this source/phase
            t_shift = t + (math.radians(ph_deg) / (2.0 * math.pi * f_hz))
            # vector from source -> grid point
            r_vec = np.stack([(X - sx), (Y - sy), np.zeros_like(X)], axis=-1)  # shape (n,n,3)

            # compute force per point
            # compute_force expects 1 vector at a time; loop in tiles for clarity
            for i in range(n):
                for j in range(n):
                    F = compute_force(
                        k=k, Q=Q, f_hz=f_hz, M=mass,
                        r_vec=r_vec[i, j, :], t=t_shift,
                        waveform_func=wave,
                        theta_deg=0.0,
                        medium_scale=1.0  # vacuum: no screening
                    )
                    Fx[i, j] += F[0]
                    Fy[i, j] += F[1]

    Fmag = np.sqrt(Fx * Fx + Fy * Fy)

    # outputs
    np.savetxt(os.path.join(out_dir, "force_magnitude.csv"), Fmag, delimiter=",", fmt="%.6e")

    fig, ax = plt.subplots(figsize=(8, 6))
    h = ax.imshow(Fmag, extent=[X.min(), X.max(), Y.min(), Y.max()],
                  origin="lower", cmap="inferno", aspect="auto")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_title("Force Magnitude (N)")
    plt.colorbar(h, ax=ax, label="|F| (N)")
    plt.tight_layout()
    fig.savefig(os.path.join(out_dir, "force_magnitude.png"))
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.quiver(X, Y, Fx, Fy, scale=50)
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_title("Force Vector Field")
    plt.tight_layout()
    fig.savefig(os.path.join(out_dir, "vector_field.png"))
    plt.close(fig)

    return {"force_x": Fx, "force_y": Fy}
