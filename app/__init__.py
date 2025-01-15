from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config
db = SQLAlchemy()

def create_app(config_name):
    """
    Factory function to create the Flask application.
    """
    # Initialize application and configuration
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize extensions
    db.init_app(app)

    # Register Blueprints
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
