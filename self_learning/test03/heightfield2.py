import pybullet as p
import pybullet_data as pd
import math
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pd.getDataPath())

textureId = -1

useProgrammatic = 0
useTerrainFromPNG = 1
useDeepLocoCSV = 2
updateHeightfield = False

heightfieldSource = useProgrammatic
import random

random.seed(10)
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
heightPerturbationRange = 0.05
if heightfieldSource == useProgrammatic:
    numHeightfieldRows = 256
    numHeightfieldColumns = 256
    heightfieldData = [0] * numHeightfieldRows * numHeightfieldColumns
    for j in range(int(numHeightfieldColumns / 2)):
        for i in range(int(numHeightfieldRows / 2)):
            height = random.uniform(0, heightPerturbationRange)
            heightfieldData[2 * i + 2 * j * numHeightfieldRows] = height
            heightfieldData[2 * i + 1 + 2 * j * numHeightfieldRows] = height
            heightfieldData[2 * i + (2 * j + 1) * numHeightfieldRows] = height
            heightfieldData[2 * i + 1 + (2 * j + 1) * numHeightfieldRows] = height

    terrainShape = p.createCollisionShape(shapeType=p.GEOM_HEIGHTFIELD, meshScale=[.05, .05, 1],
                                          heightfieldTextureScaling=(numHeightfieldRows - 1) / 2,
                                          heightfieldData=heightfieldData, numHeightfieldRows=numHeightfieldRows,
                                          numHeightfieldColumns=numHeightfieldColumns)
    terrain = p.createMultiBody(0, terrainShape)
    p.resetBasePositionAndOrientation(terrain, [0, 0, 0], [0, 0, 0, 1])

if heightfieldSource == useDeepLocoCSV:
    terrainShape = p.createCollisionShape(shapeType=p.GEOM_HEIGHTFIELD, meshScale=[.5, .5, 2.5],
                                          fileName="heightmaps/ground0.txt", heightfieldTextureScaling=128)
    terrain = p.createMultiBody(0, terrainShape)
    p.resetBasePositionAndOrientation(terrain, [0, 0, 0], [0, 0, 0, 1])

if heightfieldSource == useTerrainFromPNG:
    terrainShape = p.createCollisionShape(shapeType=p.GEOM_HEIGHTFIELD, meshScale=[.1, .1, 24],
                                          fileName="heightmaps/wm_height_out.png")
    textureId = p.loadTexture("heightmaps/gimp_overlay_out.png")
    terrain = p.createMultiBody(0, terrainShape)
    p.changeVisualShape(terrain, -1, textureUniqueId=textureId)


p.changeVisualShape(terrain, -1, rgbaColor=[1, 1, 1, 1])
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)
while (p.isConnected()):
    time.sleep(1/240)