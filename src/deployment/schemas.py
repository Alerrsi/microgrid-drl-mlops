from datetime import datetime

import numpy as np
from pydantic import BaseModel, ConfigDict, computed_field

from src.deployment.ppo import model


# clase que dictamina que información debe recibir el endpoint al modelo mediante POST
class BatteryCreate(BaseModel):
    name: str
    SoC: float
    time: datetime
    demand: float


# clase que determina la respuesta
class BatteryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    SoC: float
    time: datetime
    demand: float

    @computed_field
    @property
    def prediction(self) -> dict:
        data = np.array([self.SoC, self.demand, self.time.hour], dtype=np.float32)

        predict, _ = model.predict(data, deterministic=True)

        action = "Using Battery" if predict < 0 else "Charging battery"

        return {"Action": action, "Prediction": float(predict[0])}


class BaterryPrediction(Basemodel):
    pass
