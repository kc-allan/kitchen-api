"""
This is the main blueprint package that will contain the main views of the application.
"""
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors