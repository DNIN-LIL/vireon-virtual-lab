import numpy as np
import matplotlib.pyplot as plt

def update_particles(positions, velocities, accelerations, dt):
    velocities += accelerations * dt
    positions += velocities * dt
    return positions, velocities

def demo_run_simulation():
    num_particles = 100
    steps = 500
    field_freq = 5.0
    positions = np.random.rand(num_particles, 2)
    velocities = np.zeros_like(positions)

    for t in range(steps):
        force = np.sin(2 * np.pi * field_freq * (t / steps))
        velocities += force * 0.01
        positions += velocities * 0.01

        if t % 50 == 0:
            plt.clf()
            plt.scatter(positions[:, 0], positions[:, 1], c='red')
            plt.xlim(0, 1)
            plt.ylim(0, 1)
            plt.title(f"Step {t}")
            plt.pause(0.01)
    plt.show()