import pybullet as p
import pybullet_data
from motion_imitation import model_reader



physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
startPos = [0,0,1]
startOrientation = p.getQuaternionFromEuler([0,0,0])
robot_id = p.loadURDF("a1/a1.urdf",startPos, startOrientation)

motion_file = "/home/sz/legged/legged_robot_sheffield/motion_imitation/data/motions/a1_pace.txt"
model_file = "/home/sz/legged/legged_robot_sheffield/motion_imitation/data/policies/a1_pace.zip"
env = model_reader.get_env(motion_file)
model = model_reader.read_model(motion_file, model_file)

# 可以使用的关节
available_joints_indexes = [i for i in range(p.getNumJoints(robot_id)) if p.getJointInfo(robot_id, i)[2] != p.JOINT_FIXED]

print([p.getJointInfo(robot_id, i)[1] for i in available_joints_indexes])

joint_link_tuples = [(p.getJointInfo(robot_id, i)[0], p.getJointInfo(robot_id, i)[1].decode("utf-8"), p.getJointInfo(robot_id, i)[8], p.getJointInfo(robot_id, i)[9])  # 0:序号 1:名称 8:位移最小值 9:位移最大值
    for i in range(p.getNumJoints(robot_id))
    if p.getJointInfo(robot_id, i)[2] != p.JOINT_FIXED]

position = [p.addUserDebugParameter(
    paramName=joint_link_tuples[i][1] + " " +str(i),
    rangeMin=joint_link_tuples[i][2],
    rangeMax=joint_link_tuples[i][3],
    startValue=0
) for i in range(len(joint_link_tuples))]

# joint_velocities_params_ids = [p.addUserDebugParameter(
#     paramName=joint_link_tuples[i][1] + "V",
#     rangeMin=-50,
#     rangeMax=50,
#     startValue=0
# ) for i in range(len(joint_link_tuples))]
#
# joint_force_params_ids = [p.addUserDebugParameter(
#     paramName=joint_link_tuples[i][1] + " F",
#     rangeMin=-100,
#     rangeMax=100,
#     startValue=0
# ) for i in range(len(joint_link_tuples))]

# 添加按钮控件
btn = p.addUserDebugParameter(
    paramName="reset",
    rangeMin=1,
    rangeMax=0,
    startValue=0
)
previous_btn_value = p.readUserDebugParameter(btn)

# p.createConstraint(robot_id,-1, -1, -1,p.JOINT_FIXED,[0, 0, 0], [0, 0, 0], [0, 0, 1])
p.setRealTimeSimulation(1)
# 开启实时模拟
o = env.reset()
index = 1
while True:
    index += 1
    p.stepSimulation()
    if(index > 100):
        a, _ = model.predict(o, deterministic=True)
        o, r, done, info = env.step(a)
        if done:
            o = env.reset()
        # 将控件的参数值作为输入控制机器人，先获取各组控件值
        indices = [i for i, _, _, _ in joint_link_tuples]
        # positions = [p.readUserDebugParameter(param_id) for param_id in position]
        # velocity = [p.readUserDebugParameter(param_id) for param_id in joint_velocities_params_ids]
        # forces = [p.readUserDebugParameter(param_id) for param_id in joint_force_params_ids]
        p.setJointMotorControlArray(
            bodyUniqueId=robot_id,
            jointIndices=indices,
            controlMode=p.POSITION_CONTROL,
            targetPositions=a,
            # targetVelocities = velocity,
            # forces=forces,
        )
    else:
        # 将控件的参数值作为输入控制机器人，先获取各组控件值
        indices = [i for i, _,_,_ in joint_link_tuples]
        # positions = [p.readUserDebugParameter(param_id) for param_id in position]
        # velocity = [p.readUserDebugParameter(param_id) for param_id in joint_velocities_params_ids]
        # forces = [p.readUserDebugParameter(param_id) for param_id in joint_force_params_ids]
        p.setJointMotorControlArray(
            bodyUniqueId=robot_id,
            jointIndices=indices,
            controlMode=p.POSITION_CONTROL,
            targetPositions=[0, 0.9, -1.8, 0, 0.9, -1.8, 0, 0.9, -1.8, 0, 0.9, -1.8],
            # targetVelocities = velocity,
            # forces=forces,

        )
    # 如果按钮的累加值发生变化了，说明clicked了
    if p.readUserDebugParameter(btn) != previous_btn_value:
        # 重置速度
        for i in range(p.getNumJoints(robot_id)):
            p.setJointMotorControl2(robot_id, i, p.VELOCITY_CONTROL, 0, 0)

        # 重置位置
        p.resetBasePositionAndOrientation(robot_id, [0, 0, 1], [0, 0, 0, 1])
        previous_btn_value = p.readUserDebugParameter(btn)

p.disconnect()
