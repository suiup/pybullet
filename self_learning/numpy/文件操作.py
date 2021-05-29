list = []
with open("data.txt", "r") as f:
    data = f.readlines()
    for line in data:
        line = line.strip('\n')
        list.append(line)

print(list)
str = ",\t".join(i for i in list)
with open("test.txt", "w") as f:
    f.write(str)