import numpy as np

a1 = np.array([1, 2, 3, 4, 5])
print(a1)

a2 = np.array([[1, 2, 3, 4, 5]
                  , [6, 7, 8, 9, 10]])  # 2row * 5col
print(a2)

a3 = np.random.random(20)

print(a3)

a4 = np.random.uniform(-1.2, 1.2, 12)
print(a4)

a5 = np.array(np.random.uniform(-1.2, 1.2, 12), dtype=np.float32)
print(a5)

a6 = np.random.uniform(0, 0, 12)
print(a6)