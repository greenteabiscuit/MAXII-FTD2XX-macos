import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

z_raw = pd.concat([pd.read_csv(f"fftdata-1212/{str(i*10)}_fft.csv")["0"] for i in range(36)], axis=1).T.values
print(type(z_raw))
print(z_raw.shape)
z_raw = np.log10(z_raw)

maximum = z_raw.max()
minimum = z_raw.min()

print(maximum, minimum)

z = (z_raw - minimum) / (maximum - minimum)

fig = plt.figure()
ax = Axes3D(fig)

"""
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
"""
n = z.shape[0] # z.shape[0]
m = z.shape[1] # z.shape[1]
#rad = np.linspace(0, 10, m)
rad = np.linspace(0, 10**maximum // 1000, m // 2)
a = np.linspace(0, 2 * np.pi, n)
r, th = np.meshgrid(rad, a)

#z = np.random.uniform(-1, 1, (n,m))

print(z.shape)
print(z)
plt.subplot(projection="polar")

plt.pcolormesh(th, r, z, cmap = 'jet')

plt.plot(a, r, ls='none', color = 'k')
plt.title("Power Distribution With Frequency In Radial Direction (Using FFT)")
plt.grid()
plt.colorbar(label="Scaled Power")

plt.savefig('a.png')
plt.show()