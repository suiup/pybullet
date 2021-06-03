import numpy as np

data = np.array([[x for x in [y] * 10] for y in np.arange(0, 50, 5)]).reshape(20, 5)
print(data)