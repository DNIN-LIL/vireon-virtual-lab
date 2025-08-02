import numpy as np
import matplotlib.pyplot as plt
import os
from core.config_loader import load_config
from core.waveform_generator import sine, square, triangle, modulated
from core.logger import save_csv
from core.visualizer import save_plot

WAVEFORMS = {
    "sine": sine,
    "square": square,
    "triangle": triangle,
    "modulated": lambda f, t: modulated(f, t, mod_ratio=0.1)
}

def run():
    print("\n🔬 Running Waveform Shape Response")
    cfg = load_config("experiments/waveform_shape_response/config.yaml")

    Q = float(cfg.get("charge", 1e-6))
    f = float(cfg.get("frequency", 1e6))
    M = float(cfg.get("mass", 1.0))
    k = float(cfg.get("default_k", 1.0))
    waveforms = cfg.get("waveforms", ["sine", "square", "triangle"])
    out_dir = cfg.get("output_dir", "output/waveform_shape_response")
    os.makedirs(out_dir, exist_ok=True)

    t = np.linspace(0, 1, 1000)
    results = []

    for wf in waveforms:
        func = WAVEFORMS.get(wf)
        if not func:
            print(f"❌ Unknown waveform type: {wf}")
            continue

        signal = np.abs(func(f, t))
        avg_signal = np.mean(signal)
        F = k * Q * f * M * avg_signal
        results.append((wf, F))

        # Plot waveform
        save_plot(t, signal, f"{wf.title()} Waveform |F|", "Time (s)", "Amplitude", f"{out_dir}/{wf}_waveform_plot.png")

    save_csv(results, ["Waveform", "Force"], f"{out_dir}/waveform_force_results.csv")
    print(f"✅ Waveform comparison output saved to {out_dir}")
