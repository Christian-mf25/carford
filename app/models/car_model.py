from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
from dataclasses import dataclass

from app.exception.invalid_data import InvalidDataError
from app.configs.database import db


@dataclass
class Cars(db.Model):
    keys = ["color", "model", "owner_id"]

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

    @validates("color")
    def validate_color(self, _, value):
        valid_colors = ["yellow", "blue", "gray"]
        if value not in valid_colors:
            raise InvalidDataError(
                {
                    "error": "invalid color value",
                    "expected_color": valid_colors
                }
            )
        return value

    @validates("model")
    def validate_model(self, _, value):
        valid_model = ["hatch", "sedan", "convertible"]
        if value not in valid_model:
            raise InvalidDataError(
                {
                    "error": "invalid model value",
                    "expected_model": valid_model
                }
            )
        return value
