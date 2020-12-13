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

n = z.shape[0] # z.shape[0]
m = z.shape[1] # z.shape[1]
#rad = np.linspace(0, 10, m)
#rad = np.linspace(0, 10**maximum // 1000, m)
rad = np.linspace(1, m+1, m)
print("rad:", rad)
a = np.linspace(0, 2 * np.pi, n)
r, th = np.meshgrid(rad, a)

#z = np.random.uniform(-1, 1, (n,m))

print(z.shape)
print(r[0])
# print(z)
ax = plt.subplot(111, projection="polar")

plt.pcolormesh(th, np.log10(r), z, cmap = 'jet')

plt.plot(a, np.log10(r), ls='none', color = 'k')
plt.title("Power Distribution With Frequency In Radial Direction (Using FFT)")
ax.set_yticklabels([f"{10**i} Hz" for i in range(1, 5)])
plt.grid()
plt.colorbar(label="Scaled Power")

plt.savefig('a.png')
plt.show()