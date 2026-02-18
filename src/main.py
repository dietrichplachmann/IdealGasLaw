import numpy as np
from particle import Particle
from simulation import Simulation
from visualizer import Visualizer

WIDTH, HEIGHT = 800, 800
NUM_PARTICLES = 10
RADIUS = 7
SPEED = 3.0

def init_particles(n, width, height, radius, speed):
    particles = []
    for _ in range(n):
        x = np.random.uniform(radius, width - radius)
        y = np.random.uniform(radius, height - radius)
        angle = np.random.uniform(0, 2 * np.pi)
        vx = speed * np.cos(angle)
        vy = speed * np.sin(angle)
        particles.append(Particle(x, y, vx, vy, radius))
    return particles

if __name__ == "__main__":
    particles = init_particles(NUM_PARTICLES, WIDTH, HEIGHT, RADIUS, SPEED)
    for p in particles:
        print(p.pos, p.vel)
    sim = Simulation(WIDTH, HEIGHT, particles)
    viz = Visualizer(sim)
    viz.run()