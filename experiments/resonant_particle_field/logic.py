import numpy as np
import os
from core.config_loader import load_config
from core.physics import compute_force
from core.visualizer import save_plot
from core.waveform_generator import sine, square, triangle, modulated

WAVEFORMS = {
    "sine": sine,
    "square": square,
    "triangle": triangle,
    "modulated": lambda f, t: modulated(f, t, mod_ratio=0.1)
}

def run():
    print("\n🔬 Running Resonant Particle Field Simulation")
    cfg = load_config("experiments/resonant_particle_field/config.yaml")

    N       = int(cfg.get("grid_size", 5))
    f       = float(cfg.get("frequency", 1e6))
    Q       = float(cfg.get("charge", 1e-9))
    M       = float(cfg.get("mass", 1e-6))
    k       = float(cfg.get("default_k", 1.0))
    waveform_key = cfg.get("waveform", "sine")
    out_dir = cfg.get("output_dir", "output/resonant_particle_field")
    os.makedirs(out_dir, exist_ok=True)

    waveform_func = WAVEFORMS.get(waveform_key, sine)

    grid = np.linspace(-0.5, 0.5, N)
    sources = np.array([(x, y, z) for x in grid for y in grid for z in grid])
    test_point = np.array([0.0, 0.0, 0.0])
    steps = 1000
    dt = 1e-4
    t_arr = np.arange(steps) * dt
    force_trace = []

    for t in t_arr:
        F_total = np.zeros(3)
        for src in sources:
            r_vec = test_point - src
            F = compute_force(k, Q, f, M, r_vec, t, waveform_func)
            F_total += F
        force_magnitude = np.linalg.norm(F_total)
        force_trace.append(force_magnitude)

    np.savetxt(f"{out_dir}/resonance_force_trace.csv", force_trace, delimiter=",", fmt="%.4e")
    save_plot(t_arr, force_trace, "Force vs. Time", "Time (s)", "|F| (N)", f"{out_dir}/resonance_force_plot.png")
    print(f"✅ Output saved to {out_dir}")
