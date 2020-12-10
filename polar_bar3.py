import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)

n = 12
m = 8
rad = np.linspace(0, 10, m)
a = np.linspace(0, 2 * np.pi, n)
r, th = np.meshgrid(rad, a)

z = np.array([
    [0.9, 0.8, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7,],
    [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
    [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
    [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
    [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
    [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
    [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9],
    [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9],
])

print(z.shape)
print(z)
plt.subplot(projection="polar")

plt.pcolormesh(th, r, z, cmap = 'YlOrRd')

plt.plot(a, r, ls='none', color = 'k')
plt.title("Power Distribution With Frequency In Radial Direction")
plt.grid()
plt.colorbar(label="Scaled Power")
"""
arr1 = plt.arrow(0, 0.5, 0, 15, alpha = 0.5, width = 0.015,
                 edgecolor = 'black', facecolor = 'green', lw = 2, zorder = 5)
"""
plt.savefig('a.png')
plt.show()