import pybullet as p
import pybullet_data
import time
import numpy as np

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)

# data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#         0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0] * 25
#
# heightfieldData= data
#
# terrainShape_temp = p.createCollisionShape(shapeType = p.GEOM_HEIGHTFIELD,# 碰撞模型的形状
#                                       meshScale=[1, 1, 1],
#                                     # 在一个面积下边的纹理缩放， 值越大，纹理就越小。 这里应该可以做到近似的光滑，如果有上坡下坡的话
#                                       heightfieldTextureScaling= 100,
#                                       numHeightfieldRows=50, # 有多少行
#                                       numHeightfieldColumns=50, # 有多少列
#                                       heightfieldData=heightfieldData)  # 生成地形的数据
# data = np.random.uniform(-0.5,0.5, size=(50,50))
terrainShape = p.createCollisionShape(shapeType=p.GEOM_HEIGHTFIELD, meshScale=[1, 1, 1],
                                          fileName="data/terrain_100.txt", heightfieldTextureScaling=500)


terrain = p.createMultiBody(0, terrainShape)
p.resetBasePositionAndOrientation(terrain, [0, 0, 0], [0, 0, 0, 1])

# grass 107, 142, 35    ground 199,97,20  yellow 255,227,132
p.changeVisualShape(terrain, -1, rgbaColor=[1, 227 / 255.0, 132 / 255.0 ,1])


p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)

while (p.isConnected()):
    time.sleep(0.01)