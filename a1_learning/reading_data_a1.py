
# with open("data.txt", "r") as f:
#     line = f.readline()
#     data = line.split(',')
#     print(data)
#     numbers = [float(x) for x in data]
#     print(numbers)

# 读取文件，每一行转换为一个列表，存入到统一的一个列表中。
with open("test.txt", "r") as f:
    lines = f.readlines()
    numbers = []
    for line in lines:
        print(line)
        numbers.append([float(x) for x in line.split(",")])

    print(numbers)
    print(len(numbers))

list = [0, 0.9, -1.8] * 4,
print(list)



