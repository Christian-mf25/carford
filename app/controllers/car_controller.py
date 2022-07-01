from flask import jsonify, request
from app.exception.invalid_data import InvalidDataError

from app.models.car_model import Cars
from app.configs.database import db

def create_car():
	data = request.get_json()
	data["color"] = data["color"].lower()
	data["model"] = data["model"].lower()

	try:
		car = Cars(**data)
		db.session.add(car)
		db.session.commit()
		return jsonify(car), 201

	except InvalidDataError as e:
		return e.args[0], 400
