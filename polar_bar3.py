import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)

n = 12
m = 24
rad = np.linspace(0, 10, m)
a = np.linspace(0, 2 * np.pi, n)
r, th = np.meshgrid(rad, a)

z = np.random.uniform(-1, 1, (n,m))
print(z.shape)
print(z)
plt.subplot(projection="polar")

plt.pcolormesh(th, r, z, cmap = 'inferno')

plt.plot(a, r, ls='none', color = 'k') 
plt.grid()
plt.colorbar()
plt.savefig('a.png')
plt.show()