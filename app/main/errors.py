"""
This module contains the error handlers for the application.
"""
from flask import make_response

from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    """
    Error handler for 404 errors.
    """
    return make_response({'error': 'Cannot find this endpoint on our servers :('}, 404)
