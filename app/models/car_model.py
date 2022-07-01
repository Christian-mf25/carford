from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String

from app.configs.database import db

@dataclass
class Cars(db.Model):
	id: int
	color: str
	model: str
	owner_cnh: str

	__tablename__ = "tb_cars"

	id = Column(Integer, primary_key=True)
	color = Column(String(6))
	model = Column(String(11))
	owner_cnh = Column(String, ForeignKey("tb_owners.cnh"), nullable=False)

	owner = relationship("Owners", back_populates="cars")

