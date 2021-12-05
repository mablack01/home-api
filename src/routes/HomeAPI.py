from flask import Blueprint, request
import requests

# API for handling requests in relation to home data
# Utilitzes home data from the house-canary API

HOME_API_BASE = "/home/"
CANARY_API_BASE = "https://api.housecanary.com/v2/"

home_api = Blueprint('home_api', __name__)

# Testing endpoint to ensure the API is online
@home_api.route(HOME_API_BASE)
def hello_world():
    return "Hello world!"

# Endpoint that returns whether or not a property has a septic system
# Takes the home address and zipcode as parameters
# Assumes that the home address is properly formatted when sent over the request
@home_api.route(HOME_API_BASE + "/septic", methods=["GET"])
def has_septic_system():
    address = request.form.get('address')
    zip_code = request.form.get('zipcode')
    PARAMS = { "address": address, "zipcode": zip_code }
    # Assuming that we get a professional license to access the API
    # we would pass the authentication token into the request
    req = requests.get(url = CANARY_API_BASE + "property/details", params = PARAMS)
    data = req.json()
    sewer = data["sewer"]
    septic_system = True if sewer == "Septic" else False
    return septic_system

# This endpoint tests the Home API's ability to call an endpoint, 
# retrieve data, and process a response. I used a free public API
# to ensure I was grabbing data correctly, since I don't have a 
# license for the House Canary API at the moment.
@home_api.route(HOME_API_BASE + "/test", methods=["GET"])
def test_endpoint_call():
    post_id = request.form.get('post')
    PARAMS = { "postId": post_id }
    req = requests.get(url = "https://jsonplaceholder.typicode.com/comments", params = PARAMS)
    data = req.json()
    test_post = data[0]
    return test_post