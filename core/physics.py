import numpy as np

def compute_force(k, Q, f, M, r_vec, t, omega=None, waveform_func=None,
                  theta_deg=0, medium_scale=1.0):
    r_mag = np.linalg.norm(r_vec) + 1e-9
    if r_mag == 0:
        return np.zeros_like(r_vec)

    unit_vec = r_vec / r_mag
    theta_rad = np.deg2rad(theta_deg)

    signal = 1.0
    if waveform_func is not None:
        signal = np.abs(waveform_func(f, t))

    scalar = k * Q * f * M * np.cos(theta_rad) * medium_scale * signal
    return scalar * unit_vec / r_mag**2
