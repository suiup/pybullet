import numpy as np

data = np.random.uniform(-5,5, size=(50,50))
list = [i for i in data]
dataStr = ""
for i in list:
    dataStr += ",\t".join(str(j) for j in list) + "\n"
print(dataStr)
with open("test.txt", "w") as f:
    f.write(dataStr)