import pybullet as p
import pybullet_data
import time
import numpy as np

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)

# data = np.random.uniform(-0.5,0.5, size=(50,50))
terrainShape = p.createCollisionShape(shapeType=p.GEOM_HEIGHTFIELD, meshScale=[1, 1, 1],
                                      fileName="data/terrain_up_stairs.txt", heightfieldTextureScaling=5)



terrain = p.createMultiBody(0, terrainShape)
p.resetBasePositionAndOrientation(terrain, [16, 0, 3.5], [0, 0, 0, 1])
# grass 107, 142, 35    ground 199,97,20  yellow 255,227,132
p.changeVisualShape(terrain, -1, rgbaColor=[221/255.0, 200 / 255.0, 163 / 255.0 ,1])

boxId = p.loadURDF("a1/a1.urdf")

p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)

while (p.isConnected()):
    time.sleep(0.01)