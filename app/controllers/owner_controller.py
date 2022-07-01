from flask import request, jsonify
from sqlalchemy.exc import IntegrityError

from app.exception.invalid_data import InvalidDataError
from app.models.owner_model import Owners
from app.configs.database import db


def create_owner():
    data = request.get_json()
    data["name"] = data["name"].title()

    try:
        owner = Owners(**data)
        db.session.add(owner)
        db.session.commit()
        return jsonify(owner), 201

    except InvalidDataError as e:
        return e.args[0], 400

    except IntegrityError as e:
        return ({"msg": "cnh already exists"}), 409


def get_owner():
    owners = Owners.query.all()

    return jsonify(owners), 200


def update_owner(owner_id):
    data = request.get_json()

    try:
        owner = Owners.query.get(owner_id)

        for key, value in data.items():
            setattr(owner, key, value)

        db.session.add(owner)
        db.session.commit()

        return jsonify(owner), 200

    except AttributeError:
        return {"msg": "owner not found"}, 404

    except IntegrityError:
        return ({"msg": "cnh already exists"}), 409
