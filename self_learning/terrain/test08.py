import numpy as np

data = np.random.uniform(-0.5,0.5, size=(50,50))
list = [i for i in data]
dataStr = ""
for i in list:
    dataStr += ",\t".join(('%.5f' % j) for j in i) + "\n"
print(dataStr)
with open("test.txt", "w") as f:
    f.write(dataStr)