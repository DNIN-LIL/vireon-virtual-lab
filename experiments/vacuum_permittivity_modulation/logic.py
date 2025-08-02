import numpy as np
import os
from core.config_loader import load_config
from core.waveform_generator import sine, square, triangle, modulated
from core.visualizer import save_plot
from core.logger import save_csv

# Updated waveform mapping including corrected modulated function
WAVEFORMS = {
    "sine": sine,
    "square": square,
    "triangle": triangle,
    "modulated": lambda f, t: modulated(f, t, mod_ratio=0.1)
}

def run():
    print("\n🔬 Running Vacuum Permittivity Modulation Test")
    cfg = load_config("experiments/vacuum_permittivity_modulation/config.yaml")

    waveform_key = cfg.get("waveform", "sine")
    if waveform_key == "all":
        for wf in WAVEFORMS:
            cfg["waveform"] = wf
            run_single(cfg, wf)
    else:
        run_single(cfg, waveform_key)

def run_single(cfg, waveform_key):
    print(f"⚙️  Running with waveform: {waveform_key}")
    out_dir = os.path.join(cfg.get("output_dir", "output/vacuum_permittivity_modulation"), waveform_key)
    os.makedirs(out_dir, exist_ok=True)

    Q = float(cfg.get("charges", 1e-6))
    f = float(cfg.get("frequency", 1e6))
    M = float(cfg.get("mass", 1.0))
    k = float(cfg.get("default_k", 1.0))
    epsilons = [float(e) for e in cfg.get("epsilon_multipliers", [0.1, 0.5, 1.0, 2.0, 5.0, 10.0])]

    EPSILON_0 = 8.854e-12
    t = np.linspace(0, 1, 1000)
    waveform_func = WAVEFORMS[waveform_key]
    signal = np.abs(waveform_func(f, t))
    avg_signal = np.mean(signal)

    results = []
    for scale in epsilons:
        epsilon_eff = EPSILON_0 * scale
        k_eff = k / epsilon_eff
        F = k_eff * Q * f * M * avg_signal
        results.append((scale, F))

    save_csv(results, ["Epsilon Scale", "Force (N)"], f"{out_dir}/permittivity_force_response.csv")
    save_plot(
        [r[0] for r in results],
        [r[1] for r in results],
        "Force vs. Vacuum Permittivity",
        "ε₀ Multiplier",
        "Force (N)",
        f"{out_dir}/permittivity_force_plot.png"
    )
    print(f"✅ Output saved to {out_dir}")
