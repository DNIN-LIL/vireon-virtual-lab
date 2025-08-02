import numpy as np
import matplotlib.pyplot as plt
import os
from core.config_loader import load_config

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
    print("\n🔬 Running Mass Scaling at Constant Q·f")
    cfg = load_config("experiments/mass_scaling_at_constant_qf/config.yaml")

    Q       = float(get_input("Enter fixed charge (C)", cfg.get("charges"), float))
    f       = float(get_input("Enter fixed frequency (Hz)", cfg.get("frequencies"), float))
    masses  = get_input("Enter array of masses (kg)", cfg.get("masses"), lambda x: [float(m) for m in x])
    k       = float(get_input("Enter proportionality constant k", cfg.get("default_k"), float))
    out_dir = cfg.get("output_dir", "output/mass_scaling")
    os.makedirs(out_dir, exist_ok=True)

    forces = [k * Q * f * m for m in masses]

    plt.figure()
    plt.plot(masses, forces, marker='o')
    plt.xlabel("Mass (kg)")
    plt.ylabel("Force (N)")
    plt.title("Force vs. Mass (Q·f fixed)")
    plt.grid(True)
    plt.savefig(f"{out_dir}/mass_force_curve.png")
    plt.close()

    np.savetxt(
        f"{out_dir}/mass_force_data.csv",
        np.column_stack([masses, forces]),
        delimiter=",",
        header="Mass,Force",
        comments='',
        fmt="%.4e"
    )

    print(f"✅ Output saved to {out_dir}")
