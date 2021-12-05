from flask import Flask
from .routes.HomeAPI import home_api

# Creates and configures the Flask API
def flask_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.register_blueprint(home_api)
    return app