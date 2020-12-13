import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

z_raw = pd.concat([pd.read_csv(f"stftdata-1210/{str(i*10)}.csv")["0"] for i in range(36)], axis=1).T.values
print("z_raw:")
print(z_raw)
print(type(z_raw))
print("shape of raw z", z_raw.shape)

z_raw = np.log10(z_raw)

maximum = z_raw.max()
minimum = z_raw.min()

print(maximum, minimum)

z = (z_raw - minimum) / (maximum - minimum)

fig = plt.figure()
ax = Axes3D(fig)

n = z.shape[0] # z.shape[0]
m = z.shape[1] # z.shape[1]
rad = np.linspace(0, 10**maximum // 1000, m)
print("rad shape", rad.shape)
a = np.linspace(0, 2 * np.pi, n)
r, th = np.meshgrid(rad, a)

#z = np.random.uniform(-1, 1, (n,m))

print(z.shape)
print(z)
plt.subplot(projection="polar")

plt.pcolormesh(th, r, z, cmap = 'jet')

plt.plot(a, r, ls='none', color = 'k')
plt.title("Power Distribution With Frequency In Radial Direction (Using STFT)")
plt.grid()
plt.colorbar(label="Scaled Power")

plt.savefig('a.png')
plt.show()
