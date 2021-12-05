from flask import Blueprint

# API for handling requests in relation to home data
# Utilitzes home data from the house-canary API

home_api = Blueprint('home_api', __name__)

@home_api.route("/")
def hello_world():
    return "Hello world!"