import numpy as np
import os
from core.config_loader import load_config
from core.visualizer import save_plot
from core.physics import compute_force
from core.waveform_generator import sine, square, triangle, modulated

WAVEFORMS = {
    "sine": sine,
    "square": square,
    "triangle": triangle,
    "modulated": lambda f, t: modulated(f, t, mod_ratio=0.1)
}

def run():
    print("\n🔬 Running Toroidal Field Rotation Simulation")
    cfg = load_config("experiments/toroidal_field_rotation/config.yaml")

    waveform_choice = cfg.get("waveform", "sine")

    if waveform_choice == "all":
        for wf in WAVEFORMS:
            cfg["waveform"] = wf
            run_single(cfg, wf)
    else:
        run_single(cfg, waveform_choice)

def run_single(cfg, waveform_key):
    print(f"\n🌀 Running Toroidal Field: {waveform_key}")
    out_dir = os.path.join(cfg.get("output_dir", "output/toroidal_field_rotation"), waveform_key)
    os.makedirs(out_dir, exist_ok=True)

    radius      = float(cfg.get("radius", 0.2))
    num_charges = int(cfg.get("num_charges", 100))
    omega_rot   = float(cfg.get("omega_rot", 1000))
    f           = float(cfg.get("frequency", 1e6))
    Q           = float(cfg.get("charge", 1e-6))
    M           = float(cfg.get("mass", 1.0))
    k           = float(cfg.get("default_k", 1.0))
    steps       = int(cfg.get("steps", 1000))
    dt          = float(cfg.get("dt", 1e-4))

    t_arr = np.arange(steps) * dt
    force_trace = []

    waveform_func = WAVEFORMS.get(waveform_key, sine)
    angles = np.linspace(0, 2 * np.pi, num_charges, endpoint=False)
    test_point = np.array([0.0, 0.0, 0.0])

    for t in t_arr:
        F_total = np.zeros(3)
        for theta in angles:
            angle = theta + omega_rot * t
            src = np.array([radius * np.cos(angle), radius * np.sin(angle), 0.0])
            r_vec = test_point - src
            F = compute_force(k, Q, f, M, r_vec, t, waveform_func)
            F_total += F
        force_trace.append(np.linalg.norm(F_total))

    np.savetxt(f"{out_dir}/toroidal_force_trace.csv", force_trace, delimiter=",", fmt="%.4e")
    save_plot(t_arr, force_trace, "Toroidal Force vs. Time", "Time (s)", "|F| (N)", f"{out_dir}/toroidal_force_plot.png")
    print(f"✅ Output saved to {out_dir}")
