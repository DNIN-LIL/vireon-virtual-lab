import numpy as np
from typing import Callable, Optional, Sequence
from core.medium import Medium

def compute_force(
    k: float,
    Q: float,
    f_hz: float,
    M: float,
    r_vec: Sequence[float],
    t: float,
    omega: Optional[float] = None,
    waveform_func: Optional[Callable[[float, float], float]] = None,
    theta_deg: float = 0.0,
    medium_scale: Optional[float] = None,
    medium: Optional[Medium] = None
):
    """
    Generic force model used in the sweep:
      F ~ k * Q * f * M * cos(theta) * medium_scale * waveform(t)
      Direction is along r_vec, with 1/r^2 attenuation.
    If 'medium' and f_hz are provided, medium_scale is derived from medium.
    """
    r = np.asarray(r_vec, dtype=float)
    r_mag = np.linalg.norm(r) + 1e-9
    if r_mag == 0.0:
        return np.zeros_like(r)

    unit_vec = r / r_mag
    theta_rad = np.deg2rad(theta_deg)

    signal = 1.0
    if waveform_func is not None:
        signal = abs(float(waveform_func(f_hz, t)))

    # Decide screening
    if medium_scale is None and medium is not None:
        medium_scale = medium.electric_scale_at_freq(f_hz)
    elif medium_scale is None:
        medium_scale = 1.0

    scalar = float(k) * float(Q) * float(f_hz) * float(M) * np.cos(theta_rad) * float(medium_scale) * float(signal)
    return (scalar * unit_vec) / (r_mag ** 2)
