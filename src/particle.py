import numpy as np

class Particle:
    def __init__(self, x, y, vx, vy, radius=5, mass=1.0):
        self.pos = np.array([x, y], dtype=np.float64)
        self.vel = np.array([vx, vy], dtype=np.float64)
        self.radius = radius
        self.mass = mass

    def move(self, dt):
        self.pos += self.vel * dt

    @property
    def speed(self):
        return np.linalg.norm(self.vel)

    @property
    def kinetic_energy(self):
        return 0.5 * self.mass * self.speed**2