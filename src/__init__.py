from flask import Flask
from .routes.HomeAPI import home_api

# Creates and configures the Flask API
def flask_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    # Modularizing the endpoints into respective API's
    # Since this app only contains one endpoint, we can 
    # start off with 1 API for Home data. 
    # https://flask.palletsprojects.com/en/2.0.x/blueprints/
    app.register_blueprint(home_api)
    # app.register_blueprint(additional_api)
    return app