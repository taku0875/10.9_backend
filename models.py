from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from pydantic import BaseModel
from datetime import datetime

class MeasurementResult(Base):
    __tablename__ = "measurement_results"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    eye = Column(String) # "left" or "right"
    distance = Column(String) # "30cm" or "3m"
    visual_acuity = Column(Float)

class MeasurementResultCreate(BaseModel):
    eye: str
    distance: str
    visual_acuity: float
