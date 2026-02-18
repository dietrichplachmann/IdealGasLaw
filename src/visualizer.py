import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

class Visualizer:
    def __init__(self, sim, dt=0.5):
        self.anim = None
        self.sim = sim
        self.dt = dt

        self.fig, self.ax = plt.subplots(figsize=(7, 7))
        self.ax.set_xlim(0, sim.width)
        self.ax.set_ylim(0, sim.height)
        self.ax.set_aspect('equal')
        self.ax.set_facecolor('black')
        self.fig.patch.set_facecolor('black')
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        box = patches.Rectangle((0, 0), sim.width, sim.height,
                                linewidth=2, edgecolor='white', facecolor='none')
        self.ax.add_patch(box)

        self.circles = []
        for p in sim.particles:
            circle = plt.Circle(p.pos, p.radius, color='cyan', alpha=0.8)
            self.ax.add_patch(circle)
            self.circles.append(circle)

        self.stats_text = self.ax.text(
            10, sim.height - 20, '', color='white', fontsize=9, family='monospace'
        )

    def update(self, frame):
        self.sim.step(self.dt)

        for circle, p in zip(self.circles, self.sim.particles):
            circle.center = p.pos

        avg_speed = sum(p.speed for p in self.sim.particles) / len(self.sim.particles)
        self.stats_text.set_text(f"n={len(self.sim.particles)}  avg speed={avg_speed:.2f}")

        return self.circles + [self.stats_text]

    def run(self):
        self.anim = animation.FuncAnimation(
            self.fig,
            self.update,
            interval=16,
            blit=False,
            cache_frame_data=False
        )
        plt.tight_layout()
        plt.show()