import matplotlib.pyplot as plt
import os
import numpy as np

def save_plot(x, y, title="Plot", xlabel="X", ylabel="Y", filepath=None, marker=''):
    if filepath:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, marker=marker)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)

    # Turn off scientific offset notation
    ax.ticklabel_format(useOffset=False)

    if filepath:
        plt.tight_layout()
        fig.savefig(filepath)
    plt.close(fig)


def save_scatter(x, y, title="Scatter", xlabel="X", ylabel="Y", filepath=None):
    if filepath:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, c='red')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    if filepath:
        plt.savefig(filepath)
    plt.close()

def save_quiver(positions, vectors, title="Vector Field", filepath=None):
    if filepath:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
    plt.figure(figsize=(6, 6))
    X, Y = positions[:, 0], positions[:, 1]
    U, V = vectors[:, 0], vectors[:, 1]
    plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color='blue')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title)
    plt.grid(True)
    plt.axis('equal')
    if filepath:
        plt.savefig(filepath)
    plt.close()
