import os
import numpy as np
import matplotlib.pyplot as plt
from core.medium import Medium
from core.physics import compute_force
from core.waveform_generator import sine, square, triangle, modulated

def _ensure_dir(p: str):
    os.makedirs(p, exist_ok=True)

def _dt(cfg, medium: Medium):
    sr = float(cfg.get("sampling_rate", 0)) or 0.0
    return (1.0 / sr) if sr > 0.0 else float(medium.dt)

def _get_freq_hz(cfg: dict) -> float:
    if "frequency_hz" in cfg:
        return float(cfg["frequency_hz"])
    if "frequency" in cfg:
        return float(cfg["frequency"])
    return 1.0e6

def _wave_names(sel: str):
    s = (sel or "sine").lower()
    return ["sine", "square", "triangle", "modulated"] if s == "all" else [s]

def _wave_func(name: str):
    n = name.lower()
    if n == "sine":
        return sine
    if n == "square":
        return square
    if n == "triangle":
        return triangle
    if n == "modulated":
        # core.modulated(f_carrier, f_mod, t, index)
        return lambda f, t: modulated(f, f * 0.1, t, 1.0)
    return sine

def run(cfg: dict, medium: Medium):
    print("\nRunning Resonant Particle Field (Vacuum)")
    out_dir = cfg.get("output_dir", "output/resonant_particle_field")
    _ensure_dir(out_dir)

    N = int(cfg.get("grid_size", 5))
    f_hz = _get_freq_hz(cfg)
    Q = float(cfg.get("charge", 1.0e-9))
    M = float(cfg.get("mass", 1.0e-6))
    k = float(cfg.get("default_k", 1.0))
    wave_sel = str(cfg.get("waveform", "sine"))

    # timebase
    dt = _dt(cfg, medium)
    duration_s = float(cfg.get("duration_s", 1.0))
    steps = max(1, int(duration_s / dt))
    t_arr = np.arange(steps, dtype=float) * dt

    # sources in a cubic grid around origin
    grid = np.linspace(-0.5, 0.5, N)
    sources = np.array([(x, y, z) for x in grid for y in grid for z in grid], dtype=float)
    test_point = np.array([0.0, 0.0, 0.0], dtype=float)

    # vacuum scale
    scale = 1.0

    for name in _wave_names(wave_sel):
        wfunc = _wave_func(name)
        force_trace = np.zeros(steps, dtype=float)

        for idx, t in enumerate(t_arr):
            F_total = np.zeros(3, dtype=float)
            for src in sources:
                r_vec = test_point - src
                F = compute_force(
                    k=k, Q=Q, f_hz=f_hz, M=M,
                    r_vec=r_vec, t=t,
                    waveform_func=wfunc,
                    theta_deg=0.0,
                    medium_scale=scale
                )
                F_total += F
            force_trace[idx] = float(np.linalg.norm(F_total))

        np.savetxt(
            os.path.join(out_dir, f"resonance_force_trace_{name}.csv"),
            np.column_stack([t_arr, force_trace]),
            delimiter=",", fmt="%.6e",
            header="time_s,|F|_N", comments=""
        )

        fig, ax = plt.subplots()
        ax.plot(t_arr, force_trace)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("|F| (N)")
        ax.set_title(f"Force vs Time — {name.capitalize()} (Vacuum)")
        ax.grid(True)
        fig.tight_layout()
        fig.savefig(os.path.join(out_dir, f"resonance_force_plot_{name}.png"))
        plt.close(fig)
