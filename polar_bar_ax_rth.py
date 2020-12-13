import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import math
import matplotlib.ticker as mticker

z_raw = pd.concat([pd.read_csv(f"stftdata-1212/{str(i*10)}.csv")["0"] for i in range(36)], axis=1).T.values
print("z_raw:")
# print(z_raw)
print(type(z_raw))
pd.DataFrame(z_raw).to_csv("z_raw.csv")
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
rad = np.linspace(1, m+1, m)

expo = math.ceil(maximum)
print(expo)
print("rad shape", rad.shape)
print(rad)
a = np.linspace(0, 2 * np.pi, n)
r, th = np.meshgrid(rad, a)
print("r:", r[0])
print("th:", th)

#z = np.random.uniform(-1, 1, (n,m))
print("z")
print(z.shape)
print(z.max(), z.min())
ax = plt.subplot(111, projection="polar")
# ax.set_rscale('log')
ax.set_yscale('log')

plt.pcolormesh(th, r, z, cmap = 'jet')
ax.plot(a, r, ls='none', color = 'k')
# ax.set_ylim(1,12)
#ticks_loc = ax.get_yticks()
#print(ticks_loc)

# ax.set_yticks(np.logspace(1, 6, 6, base=10))
# ax.set_yticklabels(np.logspace(1, 9, 9, base=10, dtype=int))
#ticks_loc = ax.get_yticks()
#label_format = '{:,.0f}'
#ax.yaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
#ax.set_yticklabels([label_format.format(x) for x in ticks_loc])
#print(ticks_loc)
#ticks_loc = ax.get_xticks()
#print(ticks_loc)
# ax.set_yticklabels([f"{10 ** i} Hz" for i in range(1, 3, 1)])
#ax.set_yticklabels([f"{i} Hz" for i in range(3500, 24500, 3500)])
#ax.set_rlabel_position(45)

plt.title("Power Distribution With Frequency In Radial Direction (Using STFT)")
plt.grid()
plt.colorbar(label="Scaled Power")

# plt.savefig('a.png')
plt.show()
