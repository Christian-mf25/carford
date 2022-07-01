from flask import Blueprint

from app.controllers import owner_controller

bp = Blueprint("owners", __name__, url_prefix="/owners")

bp.post("")(owner_controller.create_owner)
bp.get("")(owner_controller.get_owner)
bp.patch("/<owner_id>")(owner_controller.update_owner)
