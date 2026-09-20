from stable_baselines3 import PPO

#  modelo usado y cargado para las predicicones
model = PPO.load("models/ppo_microgrid.zip")
