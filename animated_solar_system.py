import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(8,8))

sun = plt.Circle((0,0), 0.1)
ax.add_artist(sun)

theta = 0

planet, = ax.plot([], [], 'o')

def animate(i):
    theta = i * 0.05

    x = np.cos(theta)
    y = np.sin(theta)

    planet.set_data([x],[y])

    return planet,

ax.set_xlim(-2,2)
ax.set_ylim(-2,2)

ani = FuncAnimation(fig, animate, frames=500)

plt.show()
