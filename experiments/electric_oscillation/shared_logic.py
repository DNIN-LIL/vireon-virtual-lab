import os
import numpy as np
import matplotlib.pyplot as plt
from core.medium import Medium
from core.waveform_generator import sine, square, triangle, modulated
from core.logger import save_csv

def _ensure_dir(p: str):
    os.makedirs(p, exist_ok=True)

def _dt(cfg: dict, medium: Medium) -> float:
    sr = float(cfg.get("sampling_rate", 0)) or 0.0
    return (1.0 / sr) if sr > 0.0 else float(medium.dt)

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

def _plasma_scale(medium: Medium, f_hz: float) -> float:
    if not medium.is_plasma():
        return 1.0
    try:
        medium.drive_frequency = float(f_hz)
    except Exception:
        pass
    return float(medium.electric_scale())

def run_oscillation(cfg: dict, medium: Medium):
    """
    Headless runner used by all electric_oscillation/* variants.
    """
    out_dir = cfg.get("output_dir", "output/electric_oscillation/_unknown")
    _ensure_dir(out_dir)

    wf_name = str(cfg.get("waveform", "sine"))
    f_hz = float(cfg.get("frequency_hz", cfg.get("frequency", 1.0e6)))
    amp = float(cfg.get("amplitude", 1.0))       # drive amplitude (dimensionless scale)
    q = float(cfg.get("charge", cfg.get("charges", 1.0e-6)))
    m = float(cfg.get("mass", 1.0))
    k = float(cfg.get("default_k", 1.0))

    dt = _dt(cfg, medium)
    duration_s = float(cfg.get("duration_s", 1.0))
    steps = max(1, int(duration_s / dt))
    t = np.arange(steps, dtype=float) * dt

    wave = _wave_func(wf_name)
    scale = _plasma_scale(medium, f_hz)

    # Proportional electric forcing model:
    # F(t) ~ k * q * amplitude * f * m * scale * |waveform(t)|
    sig = np.abs(wave(f_hz, t))
    F = k * q * amp * f_hz * m * scale * sig

    np.savetxt(
        os.path.join(out_dir, "force_trace.csv"),
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
    ax.set_title(f"Electric Oscillation — {wf_name.capitalize()}")
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, "force_trace.png"))
    plt.close(fig)

    F_mean = float(np.mean(F))
    F_max = float(np.max(F))
    F_rms = float(np.sqrt(np.mean(F * F)))
    save_csv([(wf_name, F_mean, F_max, F_rms)],
             ["waveform", "mean_force_N", "max_force_N", "rms_force_N"],
             os.path.join(out_dir, "summary.csv"))
