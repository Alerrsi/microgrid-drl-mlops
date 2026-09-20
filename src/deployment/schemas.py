from datetime import datetime

from pandas._libs.tslibs.offsets import Hour
from pydantic import BaseModel, ConfigDict


# clase que dictamina que información debe recibir el endpoint al modelo mediante POST
class BatteryCreate(BaseModel):
    name: str
    SoC: float
    time: datetime


# clase que determina la respuesta
class BatteryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    SoC: float
    time: datetime
