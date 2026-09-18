import numpy as np
import pandas as pd
from gymnasium import Env
from gymnasium.spaces import Box
from numpy._core.numerictypes import float32
from pandas import DataFrame


class MicroGrdEnv(Env):
    def __init__(self, dataframe: DataFrame) -> None:
        super().__init__()
        self.baterry_capacity = 10.0
        self.max_pwer_kw = 5.0
        self.efficiency = 0.95
        self.current_soc = 0.5
        self.dataset = dataframe
        # acciones entre -1y 1, usando una forma unidimensaional shape = (1,)
        self.action_space = Box(low=-1, high=1, shape=(1,), dtype=float32)
        self.position = 0

    def step(self, action):

        # demanda actual

        if action[0] > 0:
            self.current_soc = self.charge_energy(action[0])
        elif action[0] < 0:
            self.current_soc = self.discharge_energy(action[0])

        energy_demand = self.dataset.iloc[self.position]["Global_active_power"]
        energy_red = self._calculate_energy_red(
            energy_demand, self.energy_required(action[0], 1.0)
        )
        reward = self._calculate_reward(energy_red)

        self.current_soc = np.clip(self.current_soc, 0.0, 1.0)
        self.position += 1

        # verificamos que siga en el rango del dataset
        terminated = self.position >= len(self.dataset) - 1

        return self._get_obs(), reward, terminated, False, {}

    def energy_required(self, a, t):
        return a * self.max_pwer_kw * t

    def charge_energy(self, action):
        return self.current_soc + (
            (self.energy_required(action, 1.0) * self.efficiency)
            / self.baterry_capacity
        )

    def discharge_energy(self, action):
        return self.current_soc + (
            self.energy_required(action, 1.0)
            / (self.baterry_capacity * self.efficiency)
        )

    def _get_obs(self) -> np.float32:
        """
        metodo que permite retorna la observación del agente
        con el SoC, energia demandada y hora.
        """
        energy_demand = self.dataset.iloc[self.position]["Global_active_power"]
        hour = self.dataset.iloc[self.position]["Hour"]
        return np.array([self.current_soc, energy_demand, hour], dtype=np.float32)

    def reset(self, seed):
        """
        permite reiniciar el entorno volviendo a la posición 0
        y el estado de la bateria en 50%
        """
        self.position = 0
        self.current_soc = 0.50

        return self._get_obs(), {}

    def _calculate_energy_red(self, demand: float, required: float) -> float:
        return demand + required

    def _calculate_reward(self, energy_red: float) -> float:
        return -max(0.0, energy_red)
