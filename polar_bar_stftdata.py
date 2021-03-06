import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import math
import matplotlib.ticker as mticker
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DATE = os.environ.get("DATE")
print(DATE)

#z_raw = pd.concat([pd.read_csv(f"stftdata-{DATE}/{str(i*10)}.csv")["0"] for i in range(36)], axis=1).T.values
#z_raw = pd.concat([pd.read_csv(f"stftdata/stftdata-{DATE}-fs-12900-div-2.5/{str(i*10)}.csv")["0"] for i in range(36)], axis=1).T.values
z_raw = pd.concat([pd.read_csv(f"stftdata/stftdata-1215-fs-12900-div-2.5/{str(i*10)}.csv")["0"][:50] for i in range(36)], axis=1).T.values
print("z_raw:")
# print(z_raw)
print(type(z_raw))
# waapd.DataFrame(z_raw).to_csv("z_raw.csv")
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


plt.pcolormesh(th, np.log10(r), z, cmap = 'jet')
ax.plot(a, np.log10(r), ls='none', color = 'k')

#ax.set_yticklabels(["", "10Hz", "", "100Hz", "", "1000Hz", "", "10000Hz"])
ax.set_yticklabels(["", "", "10Hz", "", "", "100Hz", "", ""])
ax.set_rlabel_position(45)

plt.title("Power Distribution With Frequency In Radial Direction (Using STFT)")
plt.grid()
plt.colorbar(label="Scaled Power")

plt.savefig(f'2020-{DATE}-stft-accumulated-logscale.png')
plt.show()
