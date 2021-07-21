import pybullet as p
import time
import pybullet_data

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
cartpole = p.loadURDF("cartpole.urdf")
p.setRealTimeSimulation(1)

maxForce=50000
p.setJointMotorControl2(cartpole,1,p.VELOCITY_CONTROL,targetVelocity=300,force=maxForce)
while (1):
  p.setGravity(0, 0, -10)
  js = p.getJointState(cartpole, 1)
  print("js=",js)

  # print("position=", js[0], "velocity=", js[1])
  time.sleep(0.5)
