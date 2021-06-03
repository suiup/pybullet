import numpy as np

#np.vstack():在竖直方向上堆叠

# np.hstack():在水平方向上平铺

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

data1 = np.vstack((arr1, arr2))
print(data1)

data2 = np.hstack((arr1, arr2))
print(data2)

a1=np.array([[1,2],[3,4],[5,6]])
a2=np.array([[7,8],[9,10],[11,12]])
data3 = np.vstack((a1, a2))
print(data3)
data4 = np.hstack((a1, a2))
print(data4)