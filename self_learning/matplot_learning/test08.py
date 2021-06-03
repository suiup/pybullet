import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig)
x = np.linspace(0,4*3.14,40)
y = np.sin(x)
z = x[:, np.newaxis]



ax.plot_surface(x, y, z)

plt.show()

