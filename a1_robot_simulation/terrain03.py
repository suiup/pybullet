import pybullet as p
import pybullet_data
import time
import numpy as np

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
data = [0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0]


heightfieldData= data

terrainShape = p.createCollisionShape(shapeType = p.GEOM_HEIGHTFIELD,# 碰撞模型的形状
                                      meshScale=[1, 1, 1],# 长 宽 高 (红)x (绿)y (蓝)z
                                    # 在一个面积下边的纹理缩放， 值越大，纹理就越小。 这里应该可以做到近似的光滑，如果有上坡下坡的话
                                      heightfieldTextureScaling= 5,# 四分之一方块里边，分开的块数
                                      numHeightfieldRows=5, # 有多少行
                                      numHeightfieldColumns=5, # 有多少列
                                      heightfieldData=heightfieldData)  # 生成地形的数据


terrain = p.createMultiBody(0, terrainShape)
p.resetBasePositionAndOrientation(terrain, [0, 0, 0], [0, 0, 0, 1])
p.changeVisualShape(terrain, -1, rgbaColor=[0.5, 0.5, 0.5, 1])


p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)

while (p.isConnected()):
    time.sleep(0.01)