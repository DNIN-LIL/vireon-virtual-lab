# core/medium.py
import math

class Medium:
    def __init__(self, cfg: dict):
        m = (cfg.get("medium") or {})
        self.type = str(m.get("type", "vacuum")).lower()
        self.dt = float(m.get("dt", 1.0e-4))
        self.plasma_frequency = float(m.get("plasma_frequency", 0.0))  # rad/s
        self.collision_freq = float(m.get("collision_freq", 0.0))      # rad/s
        self.relative_permittivity = float(m.get("relative_permittivity", 1.0))
        self.drive_frequency = float(m.get("drive_frequency", 0.0))    # rad/s
        self.electric_screening_mode = str(m.get("electric_screening_mode", "auto"))
        self.electric_screening_fixed = float(m.get("electric_screening_fixed", 1.0))
        self.magnetic_drag_coeff = float(m.get("magnetic_drag_coeff", 0.0))

    def is_plasma(self) -> bool:
        return self.type == "plasma"

    def electric_scale(self) -> float:
        if not self.is_plasma():
            return 1.0
        if self.electric_screening_mode == "fixed":
            return self.electric_screening_fixed
        w = self.drive_frequency
        if w <= 0.0:
            return 1.0 / max(self.relative_permittivity, 1e-6)
        wp = max(self.plasma_frequency, 0.0)
        nu = max(self.collision_freq, 0.0)
        denom = (w*w + nu*nu)
        real = 1.0 - (wp*wp / denom)
        imag_mag = (wp*wp * nu) / (w * denom) if w > 0.0 else 0.0
        eps_eff = (self.relative_permittivity * (real*real + imag_mag*imag_mag)) ** 0.5
        return 1.0 / max(eps_eff, 1e-6)

    def electric_scale_at_freq(self, f_hz: float) -> float:
        """Like electric_scale(), but compute using a provided drive frequency in Hz."""
        if not self.is_plasma():
            return 1.0
        if self.electric_screening_mode == "fixed":
            return self.electric_screening_fixed
        if f_hz <= 0.0:
            return 1.0 / max(self.relative_permittivity, 1e-6)
        w = 2.0 * math.pi * float(f_hz)
        wp = max(self.plasma_frequency, 0.0)
        nu = max(self.collision_freq, 0.0)
        denom = (w*w + nu*nu)
        real = 1.0 - (wp*wp / denom)
        imag_mag = (wp*wp * nu) / (w * denom)
        eps_eff = (self.relative_permittivity * (real*real + imag_mag*imag_mag)) ** 0.5
        return 1.0 / max(eps_eff, 1e-6)

    def velocity_drag(self) -> float:
        return max(self.collision_freq, 0.0)

    def magnetic_drag(self) -> float:
        return max(self.magnetic_drag_coeff, 0.0)
