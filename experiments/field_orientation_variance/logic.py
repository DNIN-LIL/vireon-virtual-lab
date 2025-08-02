import numpy as np
import os
from core.config_loader import load_config
from core.waveform_generator import sine
from core.physics import compute_force
from core.visualizer import save_plot

def get_input(prompt, default, cast_func):
    val = input(f"{prompt} [default: {default}]: ")
    if not val.strip():
        return cast_func(default)
    try:
        parsed = eval(val, {"__builtins__": {}})
        return cast_func(parsed)
    except Exception:
        print("⚠️ Invalid input. Using default.")
        return cast_func(default)

def run():
    print("\n🔬 Running Field Orientation Variance Simulation")
    cfg = load_config("experiments/field_orientation_variance/config.yaml")

    N       = int(get_input("Enter grid size (NxNxN)", cfg.get("grid_size"), int))
    f       = float(get_input("Enter frequency (Hz)", cfg.get("frequency"), float))
    Q       = float(get_input("Enter charge per particle (C)", cfg.get("charge"), float))
    M       = float(get_input("Enter test mass (kg)", cfg.get("mass"), float))
    mode    = str(get_input("Enter phase mode (coherent, random, linear)", cfg.get("mode"), str)).lower()
    k       = float(get_input("Enter proportionality constant k", cfg.get("default_k"), float))
    out_dir = cfg.get("output_dir", "output/field_orientation_variance")
    os.makedirs(out_dir, exist_ok=True)

    print(f"\n📋 Type Check:")
    print(f"  Q: {Q} ({type(Q)})")
    print(f"  f: {f} ({type(f)})")
    print(f"  M: {M} ({type(M)})")
    print(f"  k: {k} ({type(k)})")

    grid = np.linspace(-0.5, 0.5, N)
    sources = np.array([(x, y, z) for x in grid for y in grid for z in grid])
    test_point = np.array([0.0, 0.0, 0.0])
    steps = 1000
    dt = 1e-4
    t_arr = np.arange(steps) * dt
    force_trace = []

    if mode == "coherent":
        phases = np.zeros(len(sources))
    elif mode == "random":
        phases = np.random.uniform(0, 2 * np.pi, len(sources))
    elif mode == "linear":
        phases = np.linspace(0, 2 * np.pi, len(sources))
    else:
        print("❌ Invalid mode. Defaulting to 'coherent'.")
        phases = np.zeros(len(sources))

    for idx, t in enumerate(t_arr):
        F_total = np.zeros(3)
        for i, src in enumerate(sources):
            r_vec = test_point - src
            shifted_t = t + phases[i] / (2 * np.pi * f)
            omega = 2 * np.pi * f
            F = compute_force(k, Q, f, M, r_vec, shifted_t, omega, sine)

            F_total += F
        force_trace.append(np.linalg.norm(F_total))

    np.savetxt(f"{out_dir}/field_variance_force_trace.csv", force_trace, delimiter=",", fmt="%.4e")
    save_plot(t_arr, force_trace, "Force vs. Time", "Time (s)", "|F| (N)", f"{out_dir}/field_variance_plot.png")
    print(f"✅ Output saved to {out_dir}")
