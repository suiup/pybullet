import pybullet as p
import pybullet_data
from time import sleep

cid = p.connect(p.GUI)

p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
p.configureDebugVisualizer(p.COV_ENABLE_TINY_RENDERER, 0)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
plane_id = p.loadURDF("plane.urdf", useMaximalCoordinates=False)
robot_id = p.loadURDF("r2d2.urdf", basePosition=[0, 0, 2],useMaximalCoordinates=False)

p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)


while True:
    p.stepSimulation()

    mouse = p.getMouseEvents()
    if len(mouse):
        print(mouse)

p.disconnect(cid)