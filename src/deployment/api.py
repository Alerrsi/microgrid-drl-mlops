from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from stable_baselines3 import PPO

from src.deployment.database import Base, engine, get_db
from src.deployment.models import Battery
from src.deployment.schemas import BatteryCreate, BatteryResponse

# crea las tablas si no existen
Base.metadata.create_all(bind=engine)


# aplicación principal
app = FastAPI()


@app.post(
    "/battery",
    response_model=BatteryResponse,
    status_code=status.HTTP_201_CREATED,
)
async def batteryInformation(battery: BatteryCreate, db: Session = Depends(get_db)):
    batteryInfo = Battery(**battery.model_dump())
    db.add(batteryInfo)

    try:
        db.commit()

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Battery info is incorrect",
        )

    db.refresh(batteryInfo)  # loads the generated id from the database
    return batteryInfo
