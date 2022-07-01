from sqlalchemy import Column, Boolean, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
from dataclasses import dataclass

from app.exception.invalid_data import InvalidDataError
from app.configs.database import db


@dataclass
class Owners(db.Model):
    keys = ["cnh", "name"]
    
    owner_id: int
    cnh: str
    name: str
    opportunity: bool
    cars: str

    __tablename__ = "tb_owners"

    owner_id = Column(Integer, primary_key=True)
    cnh = Column(String(11), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    opportunity = Column(Boolean, default=True)

    cars = relationship("Cars", back_populates="owner")

    @validates("cnh")
    def validate_cnh(self, _, value):
        try:
            only_numbers = int(value)
        except:
            raise InvalidDataError(
                {
                    "error": "cnh should contain only numbers"
                }
            )
        if len(value) != 11:
            raise InvalidDataError(
                {
                    "error": "cnh must contain 11 digits"
                }
            )
        return value