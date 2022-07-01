from dataclasses import dataclass
from tokenize import String
from sqlalchemy.orm import relationship

from sqlalchemy import Column, ForeignKey, Boolean

from app.configs.database import db


@dataclass
class Owners(db.Model):
    cnh: str
    name: str
    opportunity: bool

    __tablename__ = "tb_owners"

    cnh = Column(String(11), primary_key=True)
    name = Column(String(255), nullable=False)
    opportunity = Column(Boolean)

    cars = relationship("Cars", back_populates="owner")