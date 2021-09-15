import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
startPos = [0,0,1]
startOrientation = p.getQuaternionFromEuler([0,0,0])
robot_id = p.loadURDF("a1/a1.urdf",startPos, startOrientation)

# Joint information
joint_num = p.getNumJoints(robot_id)

# The available joint
available_joints_indexes = [i for i in range(p.getNumJoints(robot_id)) if p.getJointInfo(robot_id, i)[2] != p.JOINT_FIXED]

print([p.getJointInfo(robot_id, i)[1] for i in available_joints_indexes])
# 0:index number 1: name 8: minimum displacement 9: maximum displacement
joint_link_tuples = [(p.getJointInfo(robot_id, i)[0], p.getJointInfo(robot_id, i)[1].decode("utf-8"), p.getJointInfo(robot_id, i)[8], p.getJointInfo(robot_id, i)[9])
    for i in range(p.getNumJoints(robot_id))
    if p.getJointInfo(robot_id, i)[2] != p.JOINT_FIXED]


# Add button
btn = p.addUserDebugParameter(
    paramName="reset",
    rangeMin=1,
    rangeMax=0,
    startValue=0
)
previous_btn_value = p.readUserDebugParameter(btn)

p.createConstraint(robot_id,-1, -1, -1,p.JOINT_FIXED,[0, 0, 0], [0, 0, 0], [0, 0, 1])


numbers = []
with open("data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        numbers.append([float(x) for x in line.split(",")])

length = len(numbers)
p.setPhysicsEngineParameter(numSolverIterations=9)
p.setPhysicsEngineParameter(enableConeFriction=0)
p.setRealTimeSimulation(1)
index = 0
episode = 0
while True:
    p.stepSimulation()
    # Use the parameter value of the control as input to control the robot, and obtain the value of each group of controls
    # indices = [1, 3, 4, 6, 8, 9, 11, 13, 14, 16, 18, 19]
    indices = [1, 3, 4, 6, 8, 9, 11, 13, 14, 16, 18, 19]
    if(episode < 0):
        p.setJointMotorControlArray(
            bodyUniqueId=robot_id,
            jointIndices=indices,
            controlMode=p.POSITION_CONTROL,
            targetPositions=[0, 0.9, -1.8] * 4,
        )
    else:
        index += 1
        if (index >= length):
            index = length - 1
        p.setJointMotorControlArray(
            bodyUniqueId=robot_id,
            jointIndices=indices,
            controlMode=p.POSITION_CONTROL,
            targetPositions=(numbers[index]),
        )
    episode += 1
    time.sleep(5/100)

p.disconnect()
