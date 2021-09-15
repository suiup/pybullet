import pybullet as p
import pybullet_data
import time
import numpy as np

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
shape = np.zeros(30).reshape(10,3)
shape[0][1] = 1
shape[0][2] = 1
# create list
heightfieldData= shape.flatten().tolist()

terrainShape = p.createCollisionShape(shapeType = p.GEOM_HEIGHTFIELD,# the shape of collision model
                                      meshScale=[1, 1, 1],# (red)  x, (green) y, (blue) z
                                      # the larger the value, the smaller the texture
                                      heightfieldTextureScaling= 5,# The number of divided blocks inside a quarter square
                                      numHeightfieldRows=5, # rows
                                      numHeightfieldColumns=6, # columns
                                      heightfieldData=heightfieldData)  # the data to create terrain

# create multiple body in simulation
terrain = p.createMultiBody(0, terrainShape)
p.resetBasePositionAndOrientation(terrain, [0, 0, 0], [0, 0, 0, 1])
p.changeVisualShape(terrain, -1, rgbaColor=[0.5, 0.5, 0.5, 1])

p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)

while (p.isConnected()):
    time.sleep(0.01)