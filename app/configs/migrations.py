from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):
    # Aqui vai as models...

    Migrate(app, app.db, compare_type=True)
