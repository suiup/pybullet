from stable_baselines import PPO1

model = PPO1.load("dog_pace")
print(model)