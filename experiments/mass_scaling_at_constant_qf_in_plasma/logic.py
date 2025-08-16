import os
import numpy as np
import matplotlib.pyplot as plt
from core.medium import Medium

def _ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def _dt(cfg, medium: Medium):
    sr = float(cfg.get("sampling_rate", 0)) or 0.0
    return (1.0 / sr) if sr > 0.0 else float(medium.dt)

def _get_scalar(cfg: dict, primary: str, fallback: str, default: float) -> float:
    if primary in cfg:
        return float(cfg[primary])
    if fallback in cfg:
        return float(cfg[fallback])
    return float(default)

def run(cfg: dict, medium: Medium):
    out_dir = cfg.get("output_dir", "output/mass_scaling_at_constant_qf_in_plasma")
    _ensure_dir(out_dir)

    q = _get_scalar(cfg, "charge", "charges", 1.0e-6)
    f_hz = _get_scalar(cfg, "frequency_hz", "frequencies", 1.0e6)
    masses = [float(x) for x in cfg.get("masses", [0.1, 0.5, 1.0, 5.0, 10.0])]
    k = float(cfg.get("default_k", 1.0))

    _ = _dt(cfg, medium)

    scale = medium.electric_scale_at_freq(f_hz) if medium.is_plasma() else 1.0
    forces = np.array([k * q * f_hz * m * scale for m in masses], dtype=float)

    np.savetxt(
        os.path.join(out_dir, "mass_vs_force.csv"),
        np.column_stack([masses, forces]),
        delimiter=",",
        fmt="%.6e",
        header="mass_kg,force_N",
        comments=""
    )

    fig, ax = plt.subplots()
    ax.plot(masses, forces, marker="o")
    ax.set_xlabel("Mass (kg)")
    ax.set_ylabel("Force (N)")
    ax.set_title("Force vs Mass at Constant q·f (Plasma)")
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, "mass_vs_force.png"))
    plt.close(fig)
