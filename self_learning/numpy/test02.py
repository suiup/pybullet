import numpy as np

data = np.zeros(25).reshape(5,5)
data[0][1] = 1
data[0][2] = 1
print(data)

print(data.T.flatten())

# print(data.flatten())
