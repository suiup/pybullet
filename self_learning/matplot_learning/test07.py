import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = Axes3D(fig)
[X,Y] = np.meshgrid()
X, Y = np.meshgrid(X, Y) #必须加上这段代码

Z = math.sin(X) + math.cos(Y)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()