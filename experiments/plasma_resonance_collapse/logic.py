import os
import time
import math
import numpy as np
from core.medium import Medium
from core.physics import compute_force
from core.particle_engine import update_particles
from core.visualizer import save_plot, save_scatter
from core.logger import save_csv
from core.waveform_generator import sine, square, triangle, modulated

def _ensure_dir(p: str):
    os.makedirs(p, exist_ok=True)

def _timebase(cfg: dict, medium: Medium):
    # Priority: explicit steps+dt; otherwise duration_s+sampling_rate; else medium.dt
    if "steps" in cfg and "dt" in cfg:
        steps = int(cfg["steps"])
        dt = float(cfg["dt"])
        return steps, dt
    sr = float(cfg.get("sampling_rate", cfg.get("sample_rate", 0))) or 0.0
    if sr > 0.0:
        dt = 1.0 / sr
        steps = max(1, int(float(cfg.get("duration_s", 1.0)) / dt))
        return steps, dt
    dt = float(medium.dt)
    steps = max(1, int(float(cfg.get("duration_s", 1.0)) / dt))
    return steps, dt

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

def _init_positions(N: int, R: float, rng: np.random.Generator):
    # Uniform in cube [-R, R]^3 (preserve your prior behavior)
    return rng.uniform(-R, R, size=(N, 3))

def _theta_to_unit(theta_deg: float):
    # optional directional knob if you ever need orientation; currently unused (set theta_deg=0)
    th = math.radians(float(theta_deg))
    return np.array([math.cos(th), math.sin(th), 0.0], dtype=float)

def run(cfg: dict, medium: Medium):
    out_root = cfg.get("output_dir", "output/plasma_resonance_collapse")
    _ensure_dir(out_root)

    waveform_choice = str(cfg.get("waveform", "sine")).lower()
    wave_list = ["sine", "square", "triangle", "modulated"] if waveform_choice == "all" else [waveform_choice]

    N = int(cfg.get("particles", 500))
    R = float(cfg.get("radius", 1.0))
    f_hz = float(cfg.get("frequency", cfg.get("frequency_hz", 5.0e5)))
    Q = float(cfg.get("charge", 1.0e-9))   # per particle charge scale
    M = float(cfg.get("mass", 1.0e-6))
    k = float(cfg.get("default_k", 1.0))
    theta_deg = float(cfg.get("theta", 0.0))

    steps, dt = _timebase(cfg, medium)

    # Medium factors
    scale = medium.electric_scale_at_freq(f_hz) if medium.is_plasma() else 1.0
    gamma_v = float(medium.velocity_drag())  # simple linear drag in velocity update

    # Seed and allocate
    rng = np.random.default_rng(42)
    init_pos = _init_positions(N, R, rng)

    for wf_name in wave_list:
        out_dir = os.path.join(out_root, wf_name)
        _ensure_dir(out_dir)

        # state
        positions = init_pos.copy()
        velocities = np.zeros_like(positions)
        force_trace = np.zeros(steps, dtype=float)   # average v^2 proxy for kinetic energy (arbitrary units)
        radius_trace = np.zeros(steps, dtype=float)  # mean distance from origin

        wave = _wave_func(wf_name)
        u_theta = _theta_to_unit(theta_deg)

        start = time.time()

        for step in range(steps):
            t = step * dt

            # Accumulate pairwise forces (O(N^2)). For N=500 this is heavy but acceptable for correctness.
            acc = np.zeros_like(positions)
            for i in range(N):
                Fi = np.zeros(3, dtype=float)
                pi = positions[i]
                for j in range(N):
                    if i == j:
                        continue
                    r_vec = pi - positions[j]  # from j -> i
                    # Correct call: use keyword args, include medium_scale and waveform
                    Fij = compute_force(
                        k=k, Q=Q, f_hz=f_hz, M=M,
                        r_vec=r_vec, t=t,
                        waveform_func=wave,
                        theta_deg=0.0,
                        medium_scale=scale
                    )
                    Fi += Fij
                acc[i] = Fi / M

            # Simple linear velocity drag from medium collisions
            if gamma_v > 0.0:
                acc -= gamma_v * velocities

            # Integrate
            positions, velocities = update_particles(positions, velocities, acc, dt)

            # Diagnostics
            v2 = float(np.mean(np.sum(velocities * velocities, axis=1)))
            avg_r = float(np.mean(np.linalg.norm(positions, axis=1)))
            force_trace[step] = v2
            radius_trace[step] = avg_r

            # Sparse snapshots
            if (step % 100) == 0 or (step == steps - 1):
                save_csv(positions.tolist(), ["x", "y", "z"], os.path.join(out_dir, f"positions_t{step:04d}.csv"))
                save_scatter(
                    positions[:, 0], positions[:, 1],
                    title=f"Step {step}",
                    xlabel="X", ylabel="Y",
                    filepath=os.path.join(out_dir, f"frame_{step:04d}.png")
                )

        # Traces and summaries
        save_plot(
            list(range(steps)), force_trace,
            title="Average Kinetic Proxy (⟨v²⟩)",
            xlabel="Step", ylabel="Velocity² (arb.)",
            filepath=os.path.join(out_dir, "energy.png")
        )
        save_plot(
            list(range(steps)), radius_trace,
            title="Mean Particle Radius",
            xlabel="Step", ylabel="Distance from Origin (m)",
            filepath=os.path.join(out_dir, "radius.png")
        )

        save_csv([[i, force_trace[i]] for i in range(steps)],
                 ["step", "v2_mean"],
                 os.path.join(out_dir, "collapse_trace.csv"))

        save_csv([[i, radius_trace[i]] for i in range(steps)],
                 ["step", "mean_radius_m"],
                 os.path.join(out_dir, "radius_trace.csv"))

        elapsed = time.time() - start
        save_csv([[N, R, f_hz, Q, M, k, steps, dt, scale, gamma_v, elapsed]],
                 ["particles", "radius_m", "frequency_hz", "charge_C", "mass_kg", "k",
                  "steps", "dt_s", "medium_scale", "velocity_drag", "elapsed_s"],
                 os.path.join(out_dir, "run_summary.csv"))
