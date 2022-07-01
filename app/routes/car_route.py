from flask import Blueprint

from app.controllers import car_controller

bp = Blueprint("cars", __name__, url_prefix="/cars")

bp.post("")(car_controller.create_car)