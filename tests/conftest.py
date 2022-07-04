from os import getenv
import pytest

from app.models.owner_model import Owners
from app.models.car_model import Cars
from app.configs.database import db
from app import create_app


@pytest.fixture(scope="module")
def test_app():
	app = create_app()
	app.config.from_object(getenv("DATABASE_URI"))
	with app.app_context():
		yield app

# @pytest.fixture(scope="module")
# def test_database():
# 	db.create_all()
# 	yield db
# 	db.session.remove()
# 	db.drop_all()