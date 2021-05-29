import numpy as np

data01 = np.linspace(0, 10, num=25)

print(data01)

data02 = np.zeros((5,5))
data02[0][1] = 1
data02[1][2] = 2
print(data02)
print(data02.flatten())
print('----------------------------------')
data03 = np.random.normal(size=(50, 50))
print(data03)
print('----------------data04------------------')
data04 = np.random.rand(4,3,2)# 生成指定维度的 0-1 之间的随机数
print(data04)
print('----------------data05------------------')

# np.random.randn() --> 生成指定维度的服从标准正态分布的随机数，输入参数为维度
data05_1 = np.random.randn()
print(data05_1)
data05_2 = np.random.randn(2,4)
print(data05_2)
print('----------------data06------------------')
# np.random.randint(low, high = None, size = None,dtype = 'l')--> 返回随机数或者随机数组成的array
data06 = np.random.randint(1,5)
print(data06)
print('----------------data07------------------')

#np.random.random_integers(low,high = None,size = None)-->返回范围为[low,high] 闭区间 随机整数
data07 = np.random.random_integers(1, size=5)
print(data07)

print('----------------data08------------------')

print('----------------data09------------------')
data09 = np.array([1,1,1])
str = '.'.join(str(i) for i in data09)
print(data09)