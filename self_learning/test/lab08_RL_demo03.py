import pybullet as p
from time import sleep
from pybullet_envs.bullet import CartPoleBulletEnv

env = CartPoleBulletEnv(renders=True, discrete_actions=False)

env.render()
env.reset()

for _ in range(10000):
    sleep(1 / 60)
    action = env.action_space.sample()
    obs, reward, done, _ = env.step(action)