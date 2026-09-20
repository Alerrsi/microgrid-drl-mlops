from datetime import date, datetime

from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from src.deployment.database import Base


class Battery(Base):
    __tablename__ = "battery_predictions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    SoC: Mapped[float] = mapped_column(Float())
    time: Mapped[datetime] = mapped_column(DateTime)
