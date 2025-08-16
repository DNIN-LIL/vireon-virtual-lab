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
    out_dir = cfg.get("output_dir", "output/vacuum_permittivity_modulation")
    _ensure_dir(out_dir)

    q = _get_scalar(cfg, "charge", "charges", 1.0e-6)
    f_hz = _get_scalar(cfg, "frequency_hz", "frequency", 1.0e6)
    m = float(cfg.get("mass", 1.0))
    k = float(cfg.get("default_k", 1.0))
    eps_mults = [float(x) for x in cfg.get("epsilon_multipliers", [0.1, 0.5, 1.0, 2.0, 5.0, 10.0])]

    _ = _dt(cfg, medium)  # kept for parity across experiments

    # In vacuum, use an effective scaling of 1/epsilon_multiplier
    forces = np.array([k * q * f_hz * m * (1.0 / em) for em in eps_mults], dtype=float)

    np.savetxt(
        os.path.join(out_dir, "epsilon_multiplier_vs_force.csv"),
        np.column_stack([eps_mults, forces]),
        delimiter=",",
        fmt="%.6e",
        header="epsilon_multiplier,force_N",
        comments=""
    )

    fig, ax = plt.subplots()
    ax.plot(eps_mults, forces, marker="o")
    ax.set_xscale("log")
    ax.set_xlabel("Epsilon Multiplier (×)")
    ax.set_ylabel("Force (N)")
    ax.set_title("Vacuum Permittivity Modulation — Force vs Epsilon Multiplier")
    ax.grid(True, which="both")
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, "epsilon_multiplier_vs_force.png"))
    plt.close(fig)
