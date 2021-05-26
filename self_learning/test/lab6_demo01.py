import pybullet as p
import pybullet_data
from time import sleep

use_gui = True
if use_gui:
    cid = p.connect(p.GUI)
else:
    cid = p.connect(p.DIRECT)

# 添加资源
p.setAdditionalSearchPath(pybullet_data.getDataPath())
plane_id = p.loadURDF("plane.urdf")
robot_id = p.loadURDF("r2d2.urdf", basePosition=[0, 0, 0.5])

# 配置渲染逻辑
p.configureDebugVisualizer(p.COV_ENABLE_TINY_RENDERER, 0)
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)

# 绘制直线
froms = [[1, 1, 0], [-1, 1, 0], [-1, 1, 3], [1, 1, 3]]
tos = [[-1, 1, 0], [-1, 1, 3], [1, 1, 3], [1, 1, 0]]
for f, t in zip(froms, tos):
    p.addUserDebugLine(
        lineFromXYZ=f,
        lineToXYZ=t,
        lineColorRGB=[0, 1, 0],
        lineWidth=2
    )

p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)

p.addUserDebugText(
    text="Destination",
    textPosition=[0, 1, 3],
    textColorRGB=[0, 1, 0],
    textSize=1.2,
)

p.addUserDebugText(
    text="I'm R2D2",
    textPosition=[0, 0, 1.2],
    textColorRGB=[0, 0, 1],
    textSize=1.2
)

wheel_link_tuples = [(p.getJointInfo(robot_id, i)[0], p.getJointInfo(robot_id, i)[1].decode("utf-8"))   # 0:序号 1:名称
    for i in range(p.getNumJoints(robot_id))
    if "wheel" in p.getJointInfo(robot_id, i)[1].decode("utf-8")]

wheel_velocity_params_ids = [p.addUserDebugParameter(
    paramName=wheel_link_tuples[i][1] + " V",
    rangeMin=-50,
    rangeMax=50,
    startValue=0
) for i in range(4)]

wheel_force_params_ids = [p.addUserDebugParameter(
    paramName=wheel_link_tuples[i][1] + " F",
    rangeMin=-100,
    rangeMax=100,
    startValue=0
) for i in range(4)]


while True:
    p.stepSimulation()

p.disconnect(cid)