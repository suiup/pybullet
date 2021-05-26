import gym


env = gym.make('CartPole-v0')
env.reset()

for _ in range(100):
    env.render()
    act = env.action_space.sample()
    obs, reward, done, _ = env.step(act)

env.close()

