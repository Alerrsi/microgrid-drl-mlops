import os
import sys

import pandas as pd
from stable_baselines3 import PPO

# Ajuste temporal del path para importar tu entorno correctamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.envs.microgrid_env import MicroGrdEnv

# 1. Cargar el dataset
df = pd.read_csv("data/processed/data_sampling.csv")

# 2. Instanciar el entorno
env = MicroGrdEnv(dataframe=df)

# 3. Inicializar el agente PPO con un Perceptrón Multicapa (MlpPolicy)
# verbose=1 activará los logs en consola para que veamos el proceso
model = PPO("MlpPolicy", env, verbose=1)

# 4. Iniciar el bucle de entrenamiento (10,000 pasos de tiempo para probar)
print("Iniciando entrenamiento...")
model.learn(total_timesteps=10000)

# 5. Guardar el modelo final en un archivo binario
os.makedirs("models", exist_ok=True)
model.save("models/ppo_microgrid")
print("Modelo guardado exitosamente.")
