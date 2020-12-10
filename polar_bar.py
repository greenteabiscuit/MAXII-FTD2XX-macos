import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.size"] = 14

# change theta
N = 20
theta = np.linspace(0, 2*np.pi, N, endpoint=False)
radii = 10 * np.ones(N)
width = np.pi / N
colors = plt.cm.magma(theta / (2*np.pi))

fig = plt.figure(figsize=(6,6))
ax = plt.subplot(111, projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.7)
plt.title('change theta')
plt.tight_layout()
plt.savefig("polorbar1.png",dpi=100) 
plt.show()

#change radii
N = 20
theta = np.linspace(0, 2*np.pi, N, endpoint=False)
radii = np.linspace(0,10,N)
width = np.pi / N
colors = plt.cm.magma(radii / 10)

fig = plt.figure(figsize=(6,6))
ax = plt.subplot(111, projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.7)
plt.title('change radii')
plt.tight_layout()
plt.savefig("polorbar2.png",dpi=100) 
plt.show()

#change width
N = 20
theta = np.linspace(0, 2*np.pi, N, endpoint=False)
radii = 10*np.ones(N)
width = np.linspace(0, np.pi/12, N)
colors = plt.cm.magma(width / (np.pi/12))

fig = plt.figure(figsize=(6,6))
ax = plt.subplot(111, projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.7)
plt.title('change width')
plt.tight_layout()
plt.savefig("polorbar3.png",dpi=100) 
plt.show()

#version
import matplotlib
print(matplotlib.__version__)
print(np.__version__)
#3.2.2
#1.18.5
