import numpy as np


class Simulation:
    def __init__(self, width, height, particles):
        self.width = width
        self.height = height
        self.particles = particles

    def step(self, dt):
        for p in self.particles:
            p.move(dt)
        self._handle_wall_collisions()
        self._handle_particle_collisions()

    def _handle_wall_collisions(self):
        for p in self.particles:
            if p.pos[0] - p.radius < 0 or p.pos[0] + p.radius > self.width:
                p.vel[0] *= -1
            if p.pos[1] - p.radius < 0 or p.pos[1] + p.radius > self.height:
                p.vel[1] *= -1

    def _handle_particle_collisions(self):
        for i, a in enumerate(self.particles):
            for b in self.particles[i+1:]:
                delta = b.pos - a.pos
                dist = np.linalg.norm(delta)
                if dist < a.radius + b.radius:
                    normal = delta / dist
                    rel_vel = a.vel - b.vel
                    speed = np.dot(rel_vel, normal)
                    if speed > 0:
                        a.vel -= speed * normal
                        b.vel += speed * normal