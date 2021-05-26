# encoding:utf-8
# train.py
from pybullet_envs.bullet import CartPoleBulletEnv
from stable_baselines.deepq import DQN
from time import sleep
import pybullet as p

env = CartPoleBulletEnv(renders=False, discrete_actions=True)

model = DQN(policy="MlpPolicy", env=env)

print("开始训练，稍等片刻")
model.learn(total_timesteps=10000)
model.save("./model")