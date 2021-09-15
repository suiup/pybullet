import pybullet as p
import pybullet_data as pd
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pd.getDataPath())

import random

random.seed(10)
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
heightPerturbationRange = 0.5
# set the rows and columns of the heightfield
numHeightfieldRows = 10
numHeightfieldColumns = 10
heightfieldData = [0] * numHeightfieldRows * numHeightfieldColumns
for j in range(int(numHeightfieldColumns / 2)):
    for i in range(int(numHeightfieldRows / 2)):
        height = random.uniform(0, heightPerturbationRange)
        heightfieldData[2 * i + 2 * j * numHeightfieldRows] = height
        heightfieldData[2 * i + 1 + 2 * j * numHeightfieldRows] = height
        heightfieldData[2 * i + (2 * j + 1) * numHeightfieldRows] = height
        heightfieldData[2 * i + 1 + (2 * j + 1) * numHeightfieldRows] = height
# create the shape of the terrain
terrainShape = p.createCollisionShape(shapeType=p.GEOM_HEIGHTFIELD, meshScale=[1, 1, 1],
                                      heightfieldTextureScaling=(numHeightfieldRows - 1) / 2,
                                      heightfieldData=heightfieldData, numHeightfieldRows=numHeightfieldRows,
                                      numHeightfieldColumns=numHeightfieldColumns)
terrain = p.createMultiBody(0, terrainShape)
p.resetBasePositionAndOrientation(terrain, [0, 0, 0], [0, 0, 0, 1])
# change the shape of the terrain
p.changeVisualShape(terrain, -1, rgbaColor=[1, 1, 1, 1])
# pybullet config
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)

while (p.isConnected()):
    time.sleep(0.01)