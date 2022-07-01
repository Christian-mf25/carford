from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String

from app.configs.database import db


@dataclass
class Cars(db.Model):
    car_id: int
    color: str
    model: str
    owner_id: int

    __tablename__ = "tb_cars"

    car_id = Column(Integer, primary_key=True)
    color = Column(String(6), nullable=False)
    model = Column(String(11), nullable=False)
    owner_id = Column(Integer, ForeignKey("tb_owners.owner_id"), nullable=False)

    owner = relationship("Owners", back_populates="cars")
