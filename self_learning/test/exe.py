import os
import pybullet as p
import pybullet_data
import time

# 连接物理引擎
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.resetSimulation()

# 重力
p.setGravity(0, 0, -10)

# 实时仿真
useRealTimeSim = 1
p.setRealTimeSimulation(useRealTimeSim)

# 加载地面
# p.loadURDF("plane.urdf")
p.loadSDF("stadium.sdf")

# 加载小测
car = p.loadURDF("racecar/racecar.urdf")

inactive_wheels = [3, 5, 7]
wheels = [2]

for wheel in inactive_wheels:
    p.setJointMotorControl2(car, wheel, p.VELOCITY_CONTROL, targetVelocity=0, force=0)

# 转向轮
steering = [4, 6]

# 自定义参数滑块，分别为速度，转向，驱动力
targetVelocitySlider = p.addUserDebugParameter("wheelVelocity", -10, 10, 0)
maxForceSlider = p.addUserDebugParameter("maxForce", 0, 10, 10)
steeringSlider = p.addUserDebugParameter("steering", -0.5, 0.5, 0)

# 开始仿真
while 1:
    # 读取速度，转向角度，驱动力参数
    maxForce = p.readUserDebugParameter(maxForceSlider)
    targetVelocity = p.readUserDebugParameter(targetVelocitySlider)
    steeringAngle = p.readUserDebugParameter(steeringSlider)
    # print(targetVelocity)

    # 根据上面读取到的值对关机进行设置
    for wheel in wheels:
        p.setJointMotorControl2(car,
                                wheel,
                                p.VELOCITY_CONTROL,
                                targetVelocity=targetVelocity,
                                force=maxForce)

    for steer in steering:
        p.setJointMotorControl2(car, steer, p.POSITION_CONTROL, targetPosition=steeringAngle)

    if useRealTimeSim == 0:
        p.stepSimulation()
