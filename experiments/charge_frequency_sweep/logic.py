import numpy as np
import matplotlib.pyplot as plt
import os
from core.config_loader import load_config

def to_float_list(val):
    try:
        return [float(x) for x in val]
    except:
        raise ValueError("Input must be a list of numbers.")

def get_input_array(prompt, default):
    val = input(f"{prompt} [default: {default}]: ")
    try:
        return to_float_list(eval(val)) if val.strip() else default
    except:
        print("⚠️ Invalid input. Using default.")
        return default

def get_input(prompt, default, cast=float):
    val = input(f"{prompt} [default: {default}]: ")
    try:
        return cast(val) if val.strip() else default
    except:
        print("⚠️ Invalid input. Using default.")
        return default

def run():
    print("\n🔬 Running Charge–Frequency Sweep")
    cfg = load_config("experiments/charge_frequency_sweep/config.yaml")

    charges = to_float_list(cfg.get("charges"))
    freqs   = to_float_list(cfg.get("frequencies"))
    M       = get_input("Enter test mass (kg)", cfg.get("mass"), float)
    k       = get_input("Enter proportionality constant k", cfg.get("default_k"), float)
    out_dir = cfg.get("output_dir", "output/charge_frequency_sweep")
    os.makedirs(out_dir, exist_ok=True)

    print(f"🔧 Charges: {charges}")
    print(f"🔧 Frequencies: {freqs}")
    print(f"⚙️  Mass: {M}, k: {k}")

    force_matrix = np.zeros((len(charges), len(freqs)))
    for i, Q in enumerate(charges):
        for j, f in enumerate(freqs):
            force_matrix[i][j] = float(k) * float(Q) * float(f) * float(M)

    fig, ax = plt.subplots()
    im = ax.imshow(force_matrix, cmap='plasma', origin='lower')
    ax.set_xticks(np.arange(len(freqs)))
    ax.set_yticks(np.arange(len(charges)))
    ax.set_xticklabels([f"{f:.0e}" for f in freqs])
    ax.set_yticklabels([f"{q:.0e}" for q in charges])
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Charge (C)")
    ax.set_title("Force Magnitude (N)")
    fig.colorbar(im, ax=ax)
    plt.tight_layout()
    plt.savefig(f"{out_dir}/force_matrix.png")
    plt.close()

    np.savetxt(f"{out_dir}/force_matrix.csv", force_matrix, delimiter=",", fmt="%.4e")
    print(f"✅ Output saved to {out_dir}")
