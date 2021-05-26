import random
import pybullet as p
from time import sleep
import numpy as np

# 创建碰撞箱模型
# createCollisionShape
# 创建视觉模型
# createVisualShape
# 将视觉模型和碰撞模型整合到一起，形成一个完整的物理模型对象， 并且可以加入一些额外的参数，比如质量，转动惯量
# createMultiBody


p.connect(p.GUI)
# 对可视化的某些设置， 禁用/启用线框，阴影什么的进行设置，是否可以看见
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
# 设置 重力
p.setGravity(0,0,-9.8)
# p.resetSimulation()
# 如果设置种子之后，用random() 生成的随机数都是同一个
random.seed(10)
heightPerturbationRange = 0.2
numHeightfieldRows = 100
numHeightfieldColumns = 100
# 一个 100x100的列表
heightfieldData = np.zeros(
    shape=[numHeightfieldColumns, numHeightfieldRows], dtype=np.float)
# 对上边这个列表进行赋值

sz_shape = np.zeros((200,100))


# Calculate vertices accumutively
for i in range(int(numHeightfieldColumns/2)):
    for j in range(int(numHeightfieldRows)):
        n1 = 0
        n2 = 0
        if j > 0:
            n1 = heightfieldData[i, j-1]
        if i > 0:
            n2 = heightfieldData[i-1, j]
        else:
            n2 = n1
        # random.uniform(x,y) 生成随机数，范围为 [x,y]
        noise = random.uniform(-heightPerturbationRange,
                                heightPerturbationRange)
        heightfieldData[i, j] = (n1+n2)/2 + noise
# 将数组方向调换
heightfieldData_inv = heightfieldData[::-1,:]
# 合并数组
heightfieldData_2 = np.concatenate((heightfieldData_inv, heightfieldData))
print('-----------------------')
print(heightfieldData_2)
print(heightfieldData_2.shape)
print('-----------------------')

col,row = heightfieldData_2.shape
heightfieldData_2 = heightfieldData_2.reshape(-1)
print("reshape: ", heightfieldData_2)

terrainShape = p.createCollisionShape(shapeType=p.GEOM_HEIGHTFIELD, heightfieldData=heightfieldData_2, meshScale=[0.5,0.5,1],
                                        numHeightfieldRows=row, numHeightfieldColumns=col)
terrain = p.createMultiBody(0, terrainShape)
p.resetBasePositionAndOrientation(terrain, [0, 0, 0], [0, 0, 0, 1])


# Create balls
balls = []
balls_init_pos = []
sphereRadius = 0.1
mass = 1
colSphereId = p.createCollisionShape(p.GEOM_SPHERE, radius=sphereRadius)
for i in range(10):
  for j in range(10):
    sphereUid = p.createMultiBody(
        mass,
        colSphereId,
        -1, [i * 3 * sphereRadius, j * 3 * sphereRadius, 2],
        useMaximalCoordinates=True)
    balls.append(sphereUid)
    balls_init_pos.append([i * 3 * sphereRadius, j * 3 * sphereRadius, 2])

while True:
    keys = p.getKeyboardEvents()
    for k, v in keys.items():
        if (k == p.B3G_F5 and (v & p.KEY_WAS_TRIGGERED)):
            print("Reset to initial position.")
            # for i,ball in enumerate(balls):
            #     p.resetBasePositionAndOrientation(ball, balls_init_pos[i], [0,0,0,1])

    p.stepSimulation()
    sleep(1./200.)