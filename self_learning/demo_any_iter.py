list = [True, True, False, False]

list02 = [False, False, False, False]

list03 = [True, True, True, True]

# any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
# 元素除了是 0、空、FALSE 外都算 TRUE。
# if all of the elements in list are False, then return False, else, return True
data = any(list)
print(data)

data02 = any(list02)
print(data02)
if(not data02):
    print("true")
else:
    print("false")

data03 = all(list)
print("data03: ",data03)
data04 = all(list02)
print("data04: ",data04)

data05 = all(list03)
print("data05: ", data05)