from flask import Blueprint

home_api = Blueprint('home_api', __name__)

@home_api.route("/")
def hello_world():
    return "Hello world!"