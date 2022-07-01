from flask import jsonify, request

from app.models.owner_model import Owners
from app.models.car_model import Cars
from app.configs.database import db


def create_car():
    data = request.get_json()
    data["color"] = data["color"].lower()
    data["model"] = data["model"].lower()
    owner = Owners.query.get(data["owner_id"])

    if not owner:
        return {"error": f"owner_id {data['owner_id']} not found"}, 404

    if not owner.opportunity:
        return {"error": f"This owner already has the car limit"}, 409

    try:
        car = Cars(**data)
        db.session.add(car)
        db.session.commit()

        if len(owner.cars) == 3:
            setattr(owner, "opportunity", False)
            db.session.add(owner)
            db.session.commit()

        return jsonify(car), 201

    except:
        return {"mesage": "car already exists"}, 409
