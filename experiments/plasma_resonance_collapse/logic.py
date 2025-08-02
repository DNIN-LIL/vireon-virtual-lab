import numpy as np
import os
import time
from core.config_loader import load_config
from core.physics import compute_force
from core.particle_engine import update_particles
from core.visualizer import save_plot, save_scatter
from core.logger import save_csv
from core.waveform_generator import sine, square, triangle, modulated

WAVEFORMS = {
    "sine": sine,
    "square": square,
    "triangle": triangle,
    "modulated": lambda f, t: modulated(f, t, mod_ratio=0.1)
}

def run():
    cfg = load_config("experiments/plasma_resonance_collapse/config.yaml")
    waveform_choice = cfg.get("waveform", "sine")

    if waveform_choice == "all":
        for wf in WAVEFORMS:
            cfg["waveform"] = wf
            run_single(cfg, wf)
    else:
        run_single(cfg, waveform_choice)

def run_single(cfg, waveform_key):
    print(f"\n🔬 Running Plasma Collapse: {waveform_key}")
    out_dir = os.path.join(cfg.get("output_dir", "output/plasma_resonance_collapse"), waveform_key)
    os.makedirs(out_dir, exist_ok=True)

    N      = int(cfg.get("particles", 500))
    R      = float(cfg.get("radius", 1.0))
    f      = float(cfg.get("frequency", 5e5))
    Q      = float(cfg.get("charge", 1e-9))
    M      = float(cfg.get("mass", 1e-6))
    k      = float(cfg.get("default_k", 1.0))
    steps  = int(cfg.get("steps", 1000))
    dt     = float(cfg.get("dt", 1e-5))

    waveform_func = WAVEFORMS.get(waveform_key, sine)
    print(f"⚙️  Parameters: N={N}, R={R}, f={f}, Q={Q}, M={M}, k={k}, waveform={waveform_key}")

    np.random.seed(42)
    positions = np.random.uniform(-R, R, size=(N, 3))
    velocities = np.zeros_like(positions)
    force_trace = []
    radius_trace = []

    start = time.time()

    for step in range(steps):
        t = step * dt
        acc = np.zeros_like(positions)

        for i in range(N):
            net_F = np.zeros(3)
            for j in range(N):
                if i == j:
                    continue
                r_vec = positions[i] - positions[j]
                net_F += compute_force(k, Q, f, M, r_vec, t, waveform_func)
            acc[i] = net_F / M

        positions, velocities = update_particles(positions, velocities, acc, dt)
        v2 = np.mean(np.linalg.norm(velocities, axis=1) ** 2)
        avg_r = np.mean(np.linalg.norm(positions, axis=1))
        force_trace.append(v2)
        radius_trace.append(avg_r)

        if step % 100 == 0 or step == steps - 1:
            save_csv(positions.tolist(), ["x", "y", "z"], f"{out_dir}/positions_t{step:04d}.csv")
            save_scatter(positions[:, 0], positions[:, 1], f"Step {step}", "X", "Y", f"{out_dir}/frame_{step:04d}.png")
            print(f"  Step {step}/{steps}")

    save_plot(range(steps), force_trace, "Average Kinetic Energy", "Step", "Velocity² (Arb)", f"{out_dir}/energy.png")
    save_plot(range(steps), radius_trace, "Avg. Particle Radius", "Step", "Distance from Center", f"{out_dir}/radius.png")

    save_csv([[i, f] for i, f in enumerate(force_trace)], ["Step", "Velocity²"], f"{out_dir}/collapse_trace.csv")
    save_csv([[i, r] for i, r in enumerate(radius_trace)], ["Step", "Radius"], f"{out_dir}/radius_trace.csv")

    print(f"✅ Completed in {round(time.time() - start, 2)} sec — output in {out_dir}")
