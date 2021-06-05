import pybullet as p
import pybullet_data
import time
import numpy as np

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
# z = np.array([[x**2 for x in np.linspace(0,2,20)] for y in range(20)])
terrainShape = p.createCollisionShape(shapeType=p.GEOM_HEIGHTFIELD, meshScale=[1, 1, 1],
                                          fileName="data/terrain_ground_slope.txt", heightfieldTextureScaling=400)


terrain = p.createMultiBody(0, terrainShape)
p.resetBasePositionAndOrientation(terrain, [8, 0, 2], [0, 0, 0, 1])

# grass 107, 142, 35    ground 199,97,20  yellow 255,227,132
p.changeVisualShape(terrain, -1, rgbaColor=[1, 227 / 255.0, 132 / 255.0 ,1])


p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)

while (p.isConnected()):
    time.sleep(0.01)