import pybullet as p
import pybullet_data
import numpy as np
import time
import json

"""
 a1 通过数据进行运动

 数据分析：
    每行有19个数据
    the mocap data represents the pose of the robot,
    root_position, x,y,z in world space
    root_orientation, a quaternion x,y,z,w, in world space
    then the joint poses (joint angles), 
    since there are 4 legs, each leg has 3 motors (shoulder, hip and knee) you get 12 dofs for the legs, 
    so 19 in total.

    position 3
    rotation/orientation  4

    angles: 12

    19个数

    前三个数字是 位置，接下来的4个数字是朝向，就是机器人面对的方向 四元数 接下来的12个数字是 关节角度    

    4个腿，每个腿有3个电机，所以会有12个数

"""

physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")

robot_id = p.loadURDF("a1/a1.urdf")

base_position, base_orientation = p.getBasePositionAndOrientation(robot_id)
print("base_position: ", base_position)
print("base_orientation: ", base_orientation)
# orientation: 身体 绕 x 轴（红色）旋转，绕 y 轴（绿色）轴旋转， 绕 z 轴（蓝色）旋转
p.resetBasePositionAndOrientation(robot_id, [0, 0, 1], [0, 0, 0, 1])
base_position, base_orientation = p.getBasePositionAndOrientation(robot_id)
print("base_position: ", base_position)
print("base_orientation: ", base_orientation)

p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)

# p.setRealTimeSimulation(1)

with open("a1_pace.txt", "r") as f:

    new_data = json.load(f)
    data_list = list(new_data["Frames"])
    print(data_list)
    print(data_list[0])
    print(data_list[0][:3])  # 三个数，机器人当前
    print(data_list[0][3:7])  # 四个数，旋转角度
    print(data_list[0][7:])  # 12个数
    positions_list = data_list[0][7:]


index = 0
while True:
    p.stepSimulation()
    if (index == len(data_list) - 1):
        index = 0
    else:
        index += 1
    p.resetBasePositionAndOrientation(robot_id,data_list[index][:3], data_list[index][3:7])
    time.sleep(0.1)

p.disconnect()




