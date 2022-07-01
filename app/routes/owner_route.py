from flask import Blueprint

from app.controllers import owner_controller

bp = Blueprint("owners", __name__, url_prefix="/owners")

bp.post("")(owner_controller.create_owner)