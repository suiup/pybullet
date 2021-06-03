import matplotlib.pyplot as plt
import numpy as np


# z = np.array([[x * y for x in [5] * 5] for y in np.arange(0,5)])
# x, y = np.meshgrid(range(z.shape[0]), range(z.shape[1]))
# print("x:", x)
# print("y:", y)
# print("z:", z)
x = [[0,1,2,3,4],
     [0,1,2,3,4],
     [0,1,2,3,4],
     [0,1,2,3,4],
     [0,1,2,3,4]]
y = [[0,0,0,0,0],
     [1,1,1,1,1],
     [1,1,1,1,1],
     [2,2,2,2,2],
     [2,2,2,2,2]]
z = np.array([[0,0,0,0,0],
     [0,0,0,0,0],
     [5,5,5,5,5],
     [5,5,5,5,5],
     [10,10,10,10,10]])
# show hight map in 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)
plt.title('z as 3d height map')
plt.show()
