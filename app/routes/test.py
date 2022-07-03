from flask import Blueprint

from app.controllers import car_controller

bp = Blueprint("teste", __name__, url_prefix="/teste")

bp.get("")(car_controller.teste)