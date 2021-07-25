import pybullet as p
import pybullet_data
import numpy as np

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

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

robot_id = p.loadURDF("a1/a1.urdf")


position, orientation = p.getBasePositionAndOrientation(robot_id)

print(position,orientation)

p.resetBasePositionAndOrientation(robot_id, [0,0,1],[0,0,0,1])
position, orientation = p.getBasePositionAndOrientation(robot_id)
print("position: ", position)
print("orientation: ", orientation)

# 可以使用的关节
available_joints_indexes = [i for i in range(p.getNumJoints(robot_id)) if p.getJointInfo(robot_id, i)[2] != p.JOINT_FIXED]
print("available_joints_indexes: ", available_joints_indexes)
joint_states = p.getJointStates(robot_id,available_joints_indexes)
print("joint states: ", joint_states) # joint position, joint velocity, joint reaction forces 6 floats, applied joint motor torque
initialAngle = np.random.uniform(low=-0.5, high=0.5, size=(1,))


joint_link_tuples = [(p.getJointInfo(robot_id, i)[0], p.getJointInfo(robot_id, i)[1].decode("utf-8"), p.getJointInfo(robot_id, i)[8], p.getJointInfo(robot_id, i)[9])  # 0:序号 1:名称 8:位移最小值 9:位移最大值
    for i in range(p.getNumJoints(robot_id))
    if p.getJointInfo(robot_id, i)[2] != p.JOINT_FIXED]

position = [p.addUserDebugParameter(
    paramName=joint_link_tuples[i][1] + " " +str(i),
    rangeMin=joint_link_tuples[i][2],
    rangeMax=joint_link_tuples[i][3],
    startValue=0
) for i in range(len(joint_link_tuples))]


for i, index in enumerate(available_joints_indexes):
    print("i: ", i)
    print("index: ", index)
    p.resetJointState(robot_id,index,0)

p.createConstraint(robot_id,-1, -1, -1,p.JOINT_FIXED,[0, 0, 0], [0, 0, 0], [0, 0, 1])
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
p.setRealTimeSimulation(1)

while True:
    # indices = [i for i, _,_,_ in joint_link_tuples]
    positions = [p.readUserDebugParameter(param_id) for param_id in position]
    # print("indices: ", indices)
    # print("positions: ", positions)
    for i, positions in zip(available_joints_indexes, positions):
        p.resetJointState(robot_id, i,positions)
    # for index, position in zip(indices,positions):
    #     p.resetJointState(robot_id,index,position)

p.disconnect()




