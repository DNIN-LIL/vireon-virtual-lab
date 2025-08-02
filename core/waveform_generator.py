import numpy as np

def sine(f, t):
    return np.sin(2 * np.pi * f * t)

def square(f, t):
    return np.sign(np.sin(2 * np.pi * f * t))

def triangle(f, t):
    return 2 * np.abs(2 * ((t * f) % 1) - 1) - 1

def modulated(f_carrier, f_mod, t, index=1.0):
    """Amplitude-modulated sine wave (AM)"""
    return np.sin(2 * np.pi * f_carrier * t + index * np.sin(2 * np.pi * f_mod * t))

def generate_waveform(wave_type, f, duration, sample_rate=1000, mod_index=1.0):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    if wave_type == "sine":
        return t, sine(f, t)
    elif wave_type == "square":
        return t, square(f, t)
    elif wave_type == "triangle":
        return t, triangle(f, t)
    elif wave_type == "modulated":
        return t, modulated(f, f * 0.1, t, mod_index)
    else:
        raise ValueError(f"Unsupported waveform type: {wave_type}")
