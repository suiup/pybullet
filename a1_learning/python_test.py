import json

with open("a1_pace.txt", "r") as f:
    new_data = json.load(f)
    data_list = list(new_data["Frames"])
    print(data_list)
    print(data_list[0])
    print(data_list[0][:3]) # 三个数，机器人当前
    print(data_list[0][3:7]) # 四个数，旋转角度
    print(data_list[0][7:]) # 12个数

print("len: ", len(data_list))
