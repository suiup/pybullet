import pybullet as p
import pybullet_data
physicsClient = p.connect(p.GUI)#Or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
startPos = [0,0,1]
startOrientation = p.getQuaternionFromEuler([0,0,0])
robot_id = p.loadURDF("a1/a1.urdf",startPos, startOrientation)

#The information of A1 joint
joint_num = p.getNumJoints(robot_id)
print("The number of the A1 joints：", joint_num)
print("A1 information: ")
for joint_index in range(joint_num):
    info_tuple = p.getJointInfo(robot_id, joint_index)
    print(f"joint index：{info_tuple[0]}\n\
            joint name：{info_tuple[1]}\n\
            joint type：{info_tuple[2]}\n\
            Variable index of the first position of the robot：{info_tuple[3]}\n\
            Variable index of the first speed of the robot：{info_tuple[4]}\n\
            Reserved parameters：{info_tuple[5]}\n\
            The damping of the joint：{info_tuple[6]}\n\
            Coefficient of friction of joints：{info_tuple[7]}\n\
            The minimum displacement of slider and revolute(hinge) ：{info_tuple[8]}\n\
            The maximum displacement of slider和revolute(hinge)：{info_tuple[9]}\n\
            Maximum joint drive：{info_tuple[10]}\n\
            Maximum speed of joints：{info_tuple[11]}\n\
            Node name：{info_tuple[12]}\n\
            Joint axis system in local frame：{info_tuple[13]}\n\
            Joint position of parent node：{info_tuple[14]}\n\
            The joint direction of the parent node：{info_tuple[15]}\n\
            The index of the parent node, if it is the base, return -1：{info_tuple[16]}\n\n")

print("cube position and cube orn: ")
cubePos, cubeOrn = p.getBasePositionAndOrientation(robot_id)

print(cubePos,cubeOrn)
p.setRealTimeSimulation(1)

while True:
    pass

p.disconnect()
