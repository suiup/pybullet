import numpy as np
# size 100 x 100   scale: -5.0~5.0  color: yellow 255,227,132

data = np.random.uniform(-5.0,5.0, size=(100, 100))
list = [i for i in data]
dataStr = ""
for i in list:
    dataStr += ",\t".join(('%.5f' % j) for j in i) + "\n"
print(dataStr)
with open("test.txt", "w") as f:
    f.write(dataStr)