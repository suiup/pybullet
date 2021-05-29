import numpy as np

data = np.random.normal(size=(50,50))
str1 = "\n".join(str(i) for i in data)
print(str1)
print('--------------------------------------------')
list = [i for i in data]
print(list)
print('--------------------------------------------')
str2 = ""
for i in list:
    str2 += ", \t".join(str(j) for j in i)
    str2 += "\n"
with open("test.txt", "w") as f:
    f.write(str2)
