from flask import Flask
from .routes.HomeAPI import home_api

# Creates and configures the Flask API
def flask_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    # Modularizing the endpoints into respective API's for ease of
    # scalability and maintanence. Since this app only contains one 
    # endpoint, we can start off with 1 API for Home data. 
    # https://flask.palletsprojects.com/en/2.0.x/blueprints/
    app.register_blueprint(home_api)
    # app.register_blueprint(additional_api)
    return app

# A wrapper function to handle request authentication
# While this does not have functionality, I am writing
# pseudocode comments on how I would approach authentication.
# This is written for JWT authentication and a SQL database.
def auth_token(func):
    # Decorating the given func
    # Grab x-access-token from request.headers
    # If token does not exist:
    #   Return an error that the token is missing
    # else:
    #   Decode the token using the secret key.
    #   Check if the decoded key aligns with a user in the DB
    #   If the key is not found in the Database:
    #       Return an error that the token is invalid
    #   else if the key is found, but the user does not have permissions:
    #       Return a not authorized error
    #   else:
    #       Grant access to the endpoint
    # return decorated function
    print("Placeholder for security")
