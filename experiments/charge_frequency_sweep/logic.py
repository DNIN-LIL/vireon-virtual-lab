import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
import numpy as np
from core.medium import Medium  # provided by lab_runner

def _to_float_list(val):
    if val is None:
        return []
    if isinstance(val, str):
        val = [x.strip() for x in val.split(",") if x.strip()]
    return [float(x) for x in val]

def _ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def _dt_from_sampling(cfg, medium: Medium | None):
    sr = float(cfg.get("sampling_rate", 0.0)) if cfg else 0.0
    if sr > 0.0:
        return 1.0 / sr
    if medium is not None and hasattr(medium, "dt"):
        return float(medium.dt)
    return 1e-3  # fallback

def run(cfg=None, medium: Medium | None = None, *args, **kwargs):
    """
    Accepts both (cfg, medium) from the new runner and (cfg) or () from older paths.
    Any extra args/kwargs are ignored to keep this entrypoint robust.
    """
    cfg = cfg or {}
    charges = _to_float_list(cfg.get("charges"))
    freqs_hz = _to_float_list(cfg.get("frequencies"))
    mass = float(cfg.get("mass", 1.0))
    k = float(cfg.get("default_k", 1.0))
    duration_s = float(cfg.get("duration_s", 1.0))
    out_dir = cfg.get("output_dir", "output/charge_frequency_sweep")

    _ensure_dir(out_dir)
    dt = _dt_from_sampling(cfg, medium)

    # number of steps is kept for parity with other modules
    steps = max(1, int(duration_s / dt))

    # simple vacuum model: no screening
    force_matrix = np.zeros((len(charges), len(freqs_hz)), dtype=float)
    for i, Q in enumerate(charges):
        for j, f_hz in enumerate(freqs_hz):
            scale = 1.0
            force_matrix[i, j] = k * float(Q) * float(f_hz) * mass * scale

    np.savetxt(os.path.join(out_dir, "force_matrix.csv"),
               force_matrix, delimiter=",", fmt="%.6e")

    fig, ax = plt.subplots()
    im = ax.imshow(force_matrix, cmap="plasma", origin="lower", aspect="auto")
    ax.set_xticks(np.arange(len(freqs_hz)))
    ax.set_yticks(np.arange(len(charges)))
    ax.set_xticklabels([f"{f:.0e}" for f in freqs_hz])
    ax.set_yticklabels([f"{q:.0e}" for q in charges])
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Charge (C)")
    ax.set_title("Force Magnitude (N)")
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, "force_matrix.png"))
    plt.close(fig)

    return {
        "steps": steps,
        "dt": dt,
        "output_dir": out_dir,
        "shape": force_matrix.shape,
    }

# Optional legacy alias if something imports run_noargs()
def run_noargs():
    return run({})
