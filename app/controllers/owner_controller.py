from flask import request, jsonify

from app.models.owner_model import Owners
from app.configs.database import db


def create_owner():
    data = request.get_json()
    keys = ["cnh" "name" "opportunity"]
    data["name"] = data["name"].title()

    try:
        owner = Owners(**data)
        db.session.add(owner)
        db.session.commit()
        return jsonify(owner), 201

    except:
        return {"mesage": "owner already exists"}, 409
