from datetime import date, datetime
from typing import Optional

from sqlalchemy import DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.deployment.database import Base


class Battery(Base):
    __tablename__ = "batterys"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    SoC: Mapped[float] = mapped_column(Float())
    time: Mapped[datetime] = mapped_column(DateTime)
    demand: Mapped[float] = mapped_column(Float)


class BaterryPrediction:
    __tablename__ = "predictions"
    id: Mapped[int] = mapped_column(primary_key=True)
    id_battery: Mapped[int] = mapped_column(ForeignKey("battery_predictions.id"))
    battery: Mapped[Optional["Battery"]] = relationship(back_populates="empleados")
    time: Mapped[datetime] = mapped_column(Datetime)
