from sqlalchemy.exc import IntegrityError
from flask import request, jsonify

from app.services.error_treatment import filter_keys, missing_key
from app.exception.invalid_data import InvalidDataError
from app.exception.missing_key import MissingKeyError
from app.models.owner_model import Owners
from app.configs.database import db


def create_owner():
    data = request.get_json()
    incoming_keys = data.keys()
    keys = Owners.keys

    try:
        filter_keys(incoming_keys, keys)
        missing_key(incoming_keys, keys)

        data["name"] = data["name"].title()

        owner = Owners(**data)
        db.session.add(owner)
        db.session.commit()
        return jsonify(owner), 201

    except KeyError as e:
        return e.args[0], 400

    except MissingKeyError as e:
        return e.args[0], 400

    except InvalidDataError as e:
        return e.args[0], 422

    except IntegrityError as e:
        return ({"error": "cnh already exists"}), 409


def get_owner():
    owners = Owners.query.all()

    return jsonify(owners), 200

def get_opportunities():
	opportunities = Owners.query.filter(Owners.opportunity==True).all()
	return jsonify(opportunities), 200


def update_owner(owner_id):
    data = request.get_json()
    incoming_keys = data.keys()
    keys = Owners.keys


    try:
        filter_keys(incoming_keys, keys)
        owner = Owners.query.get(owner_id)

        for key, value in data.items():
            setattr(owner, key, value)

        db.session.add(owner)
        db.session.commit()

        return jsonify(owner), 200

    except AttributeError:
        return {"msg": "owner not found"}, 404

    except KeyError as e:
        return e.args[0], 400

    except IntegrityError:
        return ({"msg": "cnh already exists"}), 409
    
    except InvalidDataError as e:
        return e.args[0], 400
