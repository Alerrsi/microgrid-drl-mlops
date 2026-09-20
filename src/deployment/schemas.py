from datetime import datetime

from pydantic import BaseModel, ConfigDict


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
    prediction: float
