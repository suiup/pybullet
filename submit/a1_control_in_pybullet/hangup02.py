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

position = [p.addUserDebugParameter(
    paramName=joint_link_tuples[i][1] + " " +str(i),
    rangeMin=joint_link_tuples[i][2],
    rangeMax=joint_link_tuples[i][3],
    startValue=0
) for i in range(len(joint_link_tuples))]

# Add button
btn = p.addUserDebugParameter(
    paramName="reset",
    rangeMin=1,
    rangeMax=0,
    startValue=0
)
previous_btn_value = p.readUserDebugParameter(btn)

p.createConstraint(robot_id,-1, -1, -1,p.JOINT_FIXED,[0, 0, 0], [0, 0, 0], [0, 0, 1])

p.setRealTimeSimulation(1)
# Turn on real-time simulation
while True:
    p.stepSimulation()
    # Use the parameter value of the control as input to control the robot, and obtain the value of each group of controls
    indices = [i for i, _,_,_ in joint_link_tuples]
    positions = [p.readUserDebugParameter(param_id) for param_id in position]
    p.setJointMotorControlArray(
        bodyUniqueId=robot_id,
        jointIndices=indices,
        controlMode=p.POSITION_CONTROL,
        targetPositions=positions,
    )
    # If the cumulative value of the button changes, it means clicked
    if p.readUserDebugParameter(btn) != previous_btn_value:
        # Reset velocity
        for i in range(p.getNumJoints(robot_id)):
            p.setJointMotorControl2(robot_id, i, p.VELOCITY_CONTROL, 0, 0)

        # Reset position
        p.resetBasePositionAndOrientation(robot_id, [0, 0, 1], [0, 0, 0, 1])
        previous_btn_value = p.readUserDebugParameter(btn)

p.disconnect()
