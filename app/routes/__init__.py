from flask import Flask, Blueprint

from app.routes.owner_route import bp as bp_owner

bp_api = Blueprint("api", __name__)


def init_app(app: Flask):
    bp_api.register_blueprint(bp_owner)
    app.register_blueprint(bp_api)
