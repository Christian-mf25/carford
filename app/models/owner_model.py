from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Boolean, String, Integer

from app.configs.database import db


@dataclass
class Owners(db.Model):
    owner_id: int
    cnh: str
    name: str
    opportunity: bool
    cars: str

    __tablename__ = "tb_owners"

    owner_id = Column(Integer, primary_key=True)
    cnh = Column(String(11), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    opportunity = Column(Boolean)

    cars = relationship("Cars", back_populates="owner")
