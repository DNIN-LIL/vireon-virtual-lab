import os
import math
import numpy as np
import matplotlib.pyplot as plt
from core.medium import Medium
from core.waveform_generator import sine
from core.physics import compute_force
from core.visualizer import save_plot

def _ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def _grid_points(N: int):
    g = np.linspace(-0.5, 0.5, N)
    return np.array([(x, y, z) for x in g for y in g for z in g], dtype=float)

def _make_phases(mode: str, count: int):
    m = (mode or "coherent").lower()
    if m == "coherent":
        return np.zeros(count, dtype=float)
    if m == "random":
        return np.random.uniform(0.0, 2.0 * math.pi, size=count)
    if m == "linear":
        return np.linspace(0.0, 2.0 * math.pi, num=count, endpoint=False)
    return np.zeros(count, dtype=float)

def _dt_from_cfg(cfg: dict, medium: Medium):
    sr = float(cfg.get("sampling_rate", 0)) or 0.0
    return (1.0 / sr) if sr > 0.0 else float(medium.dt)

def run(cfg: dict, medium: Medium):
    # Parameters (mirrors config keys exactly)
    N = int(cfg.get("grid_size", 4))
    f_hz = float(cfg.get("frequency", 1.0e6))
    Q = float(cfg.get("charge", 1.0e-9))
    M = float(cfg.get("mass", 1.0e-6))
    mode = str(cfg.get("mode", "random"))
    k = float(cfg.get("default_k", 1.0))
    out_dir = cfg.get("output_dir", "output/field_orientation_variance")
    _ensure_dir(out_dir)

    # Timebase
    duration_s = float(cfg.get("duration_s", 1.0))
    dt = _dt_from_cfg(cfg, medium)
    steps = max(1, int(duration_s / dt))
    t_arr = np.arange(steps, dtype=float) * dt

    # Source arrangement and phases
    sources = _grid_points(N)
    phases = _make_phases(mode, len(sources))
    test_point = np.array([0.0, 0.0, 0.0], dtype=float)

    # Force trace over time
    force_trace = np.zeros(steps, dtype=float)

    for idx, t in enumerate(t_arr):
        F_total = np.zeros(3, dtype=float)
        # sum contributions from all sources
        for i, src in enumerate(sources):
            r_vec = test_point - src
            # phase shift as a time offset
            t_shift = t + phases[i] / (2.0 * math.pi * f_hz)
            F = compute_force(
                k=k,
                Q=Q,
                f_hz=f_hz,
                M=M,
                r_vec=r_vec,
                t=t_shift,
                waveform_func=sine,
                theta_deg=0.0,
                medium_scale=1.0  # vacuum: no screening
            )
            F_total += F
        force_trace[idx] = float(np.linalg.norm(F_total))

    # Save artifacts
    np.savetxt(os.path.join(out_dir, "field_variance_force_trace.csv"),
               force_trace, delimiter=",", fmt="%.6e")
    save_plot(
        t_arr, force_trace,
        title="Force vs. Time",
        xlabel="Time (s)",
        ylabel="|F| (N)",
        filepath=os.path.join(out_dir, "field_variance_plot.png")
    )
