from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):
    from app.models.owner_model import Owners
    from app.models.car_model import Cars

    Migrate(
        app,
        app.db,
        compare_type=True
    )
