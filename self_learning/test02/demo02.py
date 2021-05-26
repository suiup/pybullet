import pybullet as p
import time
import pybullet_data

# 连接物理引擎
physicsCilent = p.connect(p.GUI)

# 渲染逻辑 先不进行渲染，而是进行载入模型的逻辑 ， 为1的时候进行渲染
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0) # 将两侧的控件隐藏


# 添加资源路径 获取pybullet_data的绝对路径 这样，凡是在pybullet_data这个文件夹下的模型，我们都可以直接使用它们的文件名加载，而不需要再输入绝对路径了。
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# 設置重力
p.setGravity(0, 0, -10)

# 加载URDF模型，此处是加载蓝白相间的陆地
planeId = p.loadURDF("plane.urdf")
# 开始状态
startPos = [0, 0, 1]
# 从欧拉角获取四元数  （欧拉角和四元数都是看物体旋转的）
startOrientation = p.getQuaternionFromEuler([0, 0, 0])
# 加载URDF模型，此处是加载 r2d2机器人 pybullet 还可以加载 obj格式的文件（3d 打印制图）
boxId = p.loadURDF("r2d2.urdf", startPos, startOrientation)

# 按照位置和朝向重置机器人的位姿，由于我们之前已经初始化了机器人，所以此处加不加这句话没什么影响
p.resetBasePositionAndOrientation(boxId, startPos, startOrientation)

# 渲染逻辑 到这里的时候，引擎进行渲染，的 该值为0 到 1 之间引入模型
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
# 开始一千次迭代，也就是一千次交互，每次交互后停顿1/240
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/240)


# 通过boxId 获取位置与方向四元数
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print("-" * 20)
print(f"机器人的位置坐标为:{cubePos}\n机器人的朝向四元数为:{cubeOrn}")
print("-" * 20)



# 指定需要关闭的服务器  默认为0 （第一个）
p.disconnect()
