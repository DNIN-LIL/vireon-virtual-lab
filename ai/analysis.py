import numpy as np
import matplotlib.pyplot as plt
import os

def analyze_force_data(force_values):
    if not force_values:
        return {}
    return {
        "max": max(force_values),
        "min": min(force_values),
        "average": sum(force_values) / len(force_values),
        "std_dev": np.std(force_values)
    }

def analyze_force_csv(csv_path, plot=True):
    try:
        force_values = np.loadtxt(csv_path, delimiter=",", skiprows=1)
        stats = analyze_force_data(force_values.tolist())

        print(f"🔍 Analysis of {csv_path}")
        for k, v in stats.items():
            print(f"{k.capitalize()}: {v:.4e} N")

        if plot:
            plt.figure()
            plt.plot(force_values, label="|F|")
            plt.axhline(stats['average'], color='r', linestyle='--', label='Mean')
            plt.title("Force Magnitude Over Time")
            plt.xlabel("Step")
            plt.ylabel("|F| (N)")
            plt.legend()
            plt.grid(True)
            plot_path = csv_path.replace(".csv", "_analysis.png")
            plt.savefig(plot_path)
            plt.close()
            print(f"📈 Plot saved to {plot_path}")

        return stats
    except Exception as e:
        print(f"⚠️ Failed to analyze file: {e}")
        return {}