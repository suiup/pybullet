from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-10, 10, 0.04)
Y = np.arange(-10, 10, 0.04)
X, Y = np.meshgrid(X, Y) #必须加上这段代码
Z = (X**2 + Y**2 + X*Y + X + Y + 1)
# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()