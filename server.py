"""
This is the main entry point for the application. It creates the Flask app and runs it.
"""
import os

from app import create_app
from config import config

# Create the application
config_name = os.environ.get('CONFIG_NAME') or 'default'
app = create_app(config_name)

if __name__ == '__main__':
    app.run(
        host=config[config_name].HOST,
        port=config[config_name].PORT
    )
