from flask import jsonify, request
from app.exception.limit_cars import LimitCarsError

from app.services.error_treatment import filter_keys, missing_key, limit_car
from app.exception.invalid_data import InvalidDataError
from app.exception.missing_key import MissingKeyError
from app.models.owner_model import Owners
from app.models.car_model import Cars
from app.configs.database import db


def create_car():

    data = request.get_json()
    incoming_keys = data.keys()
    keys = Cars.keys

    try:
        owner = Owners.query.get(data["owner_id"])
        filter_keys(incoming_keys, keys)
        missing_key(incoming_keys, keys)
        limit_car(owner)

        data["color"] = data["color"].lower()
        data["model"] = data["model"].lower()

        car = Cars(**data)
        db.session.add(car)
        db.session.commit()

        if len(owner.cars) == 3:
            setattr(owner, "opportunity", False)
            db.session.add(owner)
            db.session.commit()

        return jsonify(car), 201

    except InvalidDataError as e:
        return e.args[0], e.code

    except MissingKeyError as e:
        return e.args[0], e.code

    except KeyError as e:
        return e.args[0], 400

    except LimitCarsError as e:
        return e.args[0], e.code

    except AttributeError as e:
        return {"error": "owner_id not found"}, 404

