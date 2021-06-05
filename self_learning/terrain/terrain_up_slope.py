from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


# z = np.array([[x**2 for x in np.linspace(0,2,20)] for y in range(20)])
z = np.array([[x**2 for x in np.linspace(0,2,20)] for y in range(20)]).transpose()
list = [i for i in z]
dataStr = ""
for i in list:
    dataStr += ",\t".join(('%.5f' % j) for j in i) + "\n"
print(dataStr)
with open("test.txt", "w") as f:
    f.write(dataStr)

x, y = np.meshgrid(range(z.shape[0]), range(z.shape[1]))

# show hight map in 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)
plt.title('z as 3d height map')
plt.show()
