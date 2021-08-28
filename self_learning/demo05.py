



def show():
    list = [i * 10 for i in range(5)]
    print(list)
    str2= str(list)
    print(str2)

    list1 = ','.join(str(i) for i in list)
    print("list1", list1)


if __name__ == "__main__":
    show()