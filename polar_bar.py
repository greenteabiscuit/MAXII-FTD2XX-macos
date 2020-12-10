
import numpy as np
import matplotlib.pyplot as plt

# Using linspace so that the endpoint of 360 is included
actual = np.radians(np.linspace(0, 360, 20))
expected = np.arange(0, 70, 10)

r, theta = np.meshgrid(expected, actual)
values = np.random.random((actual.size, expected.size))

print(theta)
print(r)
print(values)

fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
ax.contourf(theta, r, values)

plt.show()
