import pybullet as p
import time
import pybullet_data

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
cartpole = p.loadURDF("cartpole.urdf")
p.setRealTimeSimulation(1)
p.setGravity(0,0,-10)
nj=p.getNumJoints(cartpole)
print("numJoints=",nj)
ji=p.getJointInfo(cartpole,0)
print("joint 1 info=",ji)
ji_1=p.getJointInfo(cartpole,1)
print("joint 2 info=",ji_1)
js=p.getJointState(cartpole,0)
print("joint 1 state=",js)
js_1=p.getJointState(cartpole,1)
print("joint 2 state=",js_1)

p.setJointMotorControl2(cartpole,1,p.POSITION_CONTROL,targetPosition=6.28,force=80)

print('-' *40)

nj=p.getNumJoints(cartpole)
print("numJoints=",nj)
ji=p.getJointInfo(cartpole,0)
print("joint 1 info=",ji)
ji_1=p.getJointInfo(cartpole,1)
print("joint 2 info=",ji_1)
js=p.getJointState(cartpole,0)
print("joint 1 state=",js)
js_1=p.getJointState(cartpole,1)
print("joint 2 state=",js_1)
while(1):
    p.setGravity(0,0,-10)
    js=p.getJointState(cartpole,1)
    print(js)
    time.sleep(0.01)