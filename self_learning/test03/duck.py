import pybullet as p
import pybullet_data
import time

# 创建碰撞箱模型
# createCollisionShape
# 创建视觉模型
# createVisualShape
# 将视觉模型和碰撞模型整合到一起，形成一个完整的物理模型对象， 并且可以加入一些额外的参数，比如质量，转动惯量
# createMultiBody

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setPhysicsEngineParameter(numSolverIterations=10)

# 载入地面模型，useMaximalCoordinates加大坐标刻度可以加快加载
# p.loadURDF("plane100.urdf", useMaximalCoordinates=True)

terrainShape = p.createCollisionShape(shapeType=p.GEOM_HEIGHTFIELD, meshScale=[.5, .5, 2.5],
                                          fileName="heightmaps/ground0.txt", heightfieldTextureScaling=128)
terrain = p.createMultiBody(0, terrainShape)
p.resetBasePositionAndOrientation(terrain, [0, 0, 0], [0, 0, 0, 1])
p.changeVisualShape(terrain, -1, rgbaColor=[1, 1, 1, 1])


# 创建视觉模型和碰撞箱模型时共用的两个参数
shift = [0, -0.02, 0]
scale = [1, 1, 1]


# 创建过程中不渲染
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
# 不展示GUI的套件
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
# 禁用 tinyrenderer
p.configureDebugVisualizer(p.COV_ENABLE_TINY_RENDERER, 0)

p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)
# 创建视觉形状和碰撞箱形状
visual_shape_id = p.createVisualShape(
    shapeType=p.GEOM_MESH,
    fileName="duck.obj",
    rgbaColor=[1, 1, 1, 1],
    specularColor=[0.4, 0.4, 0],
    visualFramePosition=shift,
    meshScale=scale
)

collision_shape_id = p.createCollisionShape(
    shapeType=p.GEOM_MESH,
    fileName="duck_vhacd.obj",
    collisionFramePosition=shift,
    meshScale=scale
)

# 使用创建的视觉形状和碰撞箱形状使用createMultiBody将两者结合在一起
for i in range(4):
    p.createMultiBody(
        baseMass=1,
        baseCollisionShapeIndex=collision_shape_id,
        baseVisualShapeIndex=visual_shape_id,
        basePosition=[0, 0, 2],
        useMaximalCoordinates=True
    )


# 创建结束，重新开启渲染
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)

while (1):
    time.sleep(1./240.)





