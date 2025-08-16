import os
import numpy as np
import matplotlib.pyplot as plt
from core.medium import Medium
from core.waveform_generator import sine, square, triangle, modulated
from core.logger import save_csv

def _ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def _dt(cfg: dict, medium: Medium) -> float:
    sr = float(cfg.get("sampling_rate", 0)) or 0.0
    return (1.0 / sr) if sr > 0.0 else float(medium.dt)

def _get_scalar(cfg: dict, primary: str, fallback: str, default: float) -> float:
    if primary in cfg:
        return float(cfg[primary])
    if fallback in cfg:
        return float(cfg[fallback])
    return float(default)

def _wave_funcs(names):
    out = {}
    for n in names:
        key = str(n).lower()
        if key == "sine":
            out[n] = sine
        elif key == "square":
            out[n] = square
        elif key == "triangle":
            out[n] = triangle
        elif key == "modulated":
            out[n] = lambda f, t: modulated(f, f * 0.1, t, 1.0)
    return out

def run(cfg: dict, medium: Medium):
    out_dir = cfg.get("output_dir", "output/waveform_shape_response")
    _ensure_dir(out_dir)

    q = _get_scalar(cfg, "charge", "charges", 1.0e-6)
    f_hz = _get_scalar(cfg, "frequency_hz", "frequency", 1.0e6)
    m = float(cfg.get("mass", 1.0))
    k = float(cfg.get("default_k", 1.0))
    wave_names = list(cfg.get("waveforms", ["sine", "square", "triangle"]))

    dt = _dt(cfg, medium)
    duration_s = float(cfg.get("duration_s", 1.0))
    steps = max(1, int(duration_s / dt))
    t = np.arange(steps, dtype=float) * dt

    scale = 1.0  # vacuum
    funcs = _wave_funcs(wave_names)

    summary_rows = []
    for name, wf in funcs.items():
        sig = np.abs(wf(f_hz, t))
        F = k * q * f_hz * m * scale * sig

        F_mean = float(np.mean(F))
        F_max = float(np.max(F))
        F_rms = float(np.sqrt(np.mean(F * F)))
        summary_rows.append((name, F_mean, F_max, F_rms))

        wf_dir = os.path.join(out_dir, name)
        _ensure_dir(wf_dir)
        np.savetxt(
            os.path.join(wf_dir, "force_trace.csv"),
            np.column_stack([t, F]),
            delimiter=",",
            fmt="%.6e",
            header="time_s,force_N",
            comments=""
        )

        fig, ax = plt.subplots()
        ax.plot(t, F)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Force (N)")
        ax.set_title(f"Waveform Shape Response — {name.capitalize()} (Vacuum)")
        ax.grid(True)
        fig.tight_layout()
        fig.savefig(os.path.join(wf_dir, "force_trace.png"))
        plt.close(fig)

    save_csv(summary_rows,
             ["waveform", "mean_force_N", "max_force_N", "rms_force_N"],
             os.path.join(out_dir, "summary.csv"))

    labels = [r[0] for r in summary_rows]
    means = [r[1] for r in summary_rows]
    fig, ax = plt.subplots()
    ax.bar(labels, means)
    ax.set_ylabel("Mean Force (N)")
    ax.set_title("Waveform Shape Response — Mean Force (Vacuum)")
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, "mean_force_comparison.png"))
    plt.close(fig)
