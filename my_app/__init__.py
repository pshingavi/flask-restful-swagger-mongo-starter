from flask import Flask
from config import config

__author__ = 'Preetam'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name, 'default'))

    from my_app.api import api1_0 as api1_0_blueprint
    app.register_blueprint(api1_0_blueprint, url_prefix='/api/v1_0')

    return app