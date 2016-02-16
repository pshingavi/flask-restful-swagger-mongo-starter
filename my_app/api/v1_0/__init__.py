from flask import Blueprint

__author__ = 'Preetam'


# Create a blueprint for v1_0
api = Blueprint('api', __name__)

from .views import test_route