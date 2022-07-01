from flask import jsonify, request, json

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

	except:
		return {"mesage": "car already exists"}, 409