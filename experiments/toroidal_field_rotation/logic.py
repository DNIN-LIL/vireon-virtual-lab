import os
import math
import numpy as np
import matplotlib.pyplot as plt
from core.medium import Medium
from core.physics import compute_force
from core.waveform_generator import sine, square, triangle, modulated
from core.visualizer import save_plot

def _ensure_dir(p: str):
    os.makedirs(p, exist_ok=True)

def _timebase(cfg: dict, medium: Medium):
    if "steps" in cfg and "dt" in cfg:
        steps = int(cfg["steps"])
        dt = float(cfg["dt"])
        return steps, dt
    sr = float(cfg.get("sampling_rate", 0)) or 0.0
    if sr > 0.0:
        dt = 1.0 / sr
        steps = max(1, int(float(cfg.get("duration_s", 1.0)) / dt))
        return steps, dt
    dt = float(medium.dt)
    steps = max(1, int(float(cfg.get("duration_s", 1.0)) / dt))
    return steps, dt

def _wave_names(sel: str):
    s = (sel or "sine").lower()
    return ["sine", "square", "triangle", "modulated"] if s == "all" else [s]

def _wave_func(name: str):
    n = (name or "sine").lower()
    if n == "sine":
        return sine
    if n == "square":
        return square
    if n == "triangle":
        return triangle
    if n == "modulated":
        # modulated(f_carrier, f_mod, t, index)
        return lambda f, t: modulated(f, f * 0.1, t, 1.0)
    return sine

def _ring_positions(R: float, N: int, omega: float, t: float):
    idx = np.arange(N, dtype=float)
    phi = 2.0 * math.pi * idx / float(N) + omega * t
    x = R * np.cos(phi)
    y = R * np.sin(phi)
    z = np.zeros_like(x)
    return np.stack([x, y, z], axis=-1)

def run(cfg: dict, medium: Medium):
    out_root = cfg.get("output_dir", "output/toroidal_field_rotation")
    _ensure_dir(out_root)

    R = float(cfg.get("radius", 0.2))
    N = int(cfg.get("num_charges", 100))
    omega = float(cfg.get("omega_rot", 1000.0))
    f_hz = float(cfg.get("frequency_hz", cfg.get("frequency", 1.0e6)))
    q = float(cfg.get("charge", 1.0e-6))
    m = float(cfg.get("mass", 1.0))
    k = float(cfg.get("default_k", 1.0))

    steps, dt = _timebase(cfg, medium)
    t_arr = np.arange(steps, dtype=float) * dt

    names = _wave_names(str(cfg.get("waveform", "sine")))
    probe = np.array([0.0, 0.0, 0.0], dtype=float)
    scale = 1.0  # vacuum

    for name in names:
        wave = _wave_func(name)
        out_dir = os.path.join(out_root, name)
        _ensure_dir(out_dir)

        trace = np.zeros(steps, dtype=float)
        angles = np.linspace(0.0, 2.0 * math.pi, N, endpoint=False)

        for ti, t in enumerate(t_arr):
            Ftot = np.zeros(3, dtype=float)
            # ring state at time t
            phi = angles + omega * t
            pos = np.stack([R * np.cos(phi), R * np.sin(phi), np.zeros_like(phi)], axis=-1)
            for s in range(N):
                r_vec = probe - pos[s, :]
                F = compute_force(
                    k=k, Q=q, f_hz=f_hz, M=m,
                    r_vec=r_vec, t=t,
                    waveform_func=wave,
                    theta_deg=0.0,
                    medium_scale=scale
                )
                Ftot += F
            trace[ti] = float(np.linalg.norm(Ftot))

        np.savetxt(
            os.path.join(out_dir, "toroidal_force_trace.csv"),
            np.column_stack([t_arr, trace]),
            delimiter=",", fmt="%.6e",
            header="time_s,|F|_N", comments=""
        )
        save_plot(
            t_arr, trace,
            title=f"Toroidal Force vs Time — {name.capitalize()} (Vacuum)",
            xlabel="Time (s)", ylabel="|F| (N)",
            filepath=os.path.join(out_dir, "toroidal_force_plot.png")
        )
