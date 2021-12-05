from flask import Blueprint, request
from flask_restx import Api, Resource
# from ... import auth_token
import requests

# API for handling requests in relation to home data
# Utilitzes home data from the house-canary API
CANARY_API_BASE = "https://api.housecanary.com/v2/"

home_api = Blueprint('home_api', __name__)
# Adding Swagger docs
api = Api(
    home_api,
    version="1.0",
    title="Home API",
    description="A Restful API for home data",
)
ns = api.namespace("home", description="Endpoints related to homes")
api.add_namespace(ns)

# Endpoint that returns whether or not a property has a septic system
# Takes the home address and zipcode as parameters
# Assumes that the home address is properly formatted when sent over the request
@ns.route("/septic", methods=["GET"], doc={"description": "An endpoint for determining whether or not a unit has a septic system. Note that this endpoint will not complete its request as there is currently no access to the HomeCanary API, which this endpoint relies on."})
@api.doc(params={"address": "The home address", "zipcode": "The home zipcode"}, responses={200: "Success", 400: "Missing parameters"})
# @auth_token - Once implemented, we can wrap a given endpoint with the auth validation
class HasSepticSystem(Resource):
    def get(self):
        address = request.args.get('address')
        zip_code = request.args.get('zipcode')
        if address and zip_code:
            PARAMS = { "address": address, "zipcode": zip_code }
            # Assuming that we get a professional license to access the API
            # we would pass the authentication token into the request
            req = requests.get(url = CANARY_API_BASE + "property/details", params = PARAMS)
            data = req.json()
            sewer = data["sewer"]
            septic_system = True if sewer == "Septic" else False
            return {"success": True, "data": septic_system}
        else:
            return "Missing parameters", 400

# This endpoint tests the Home API's ability to call an endpoint, 
# retrieve data, and process a response. I used a free public API
# to ensure I was grabbing data correctly, since I don't have a 
# license for the House Canary API at the moment.
@ns.route("/test", methods=["GET"], doc={"description": "An endpoint for grabbing the first post meta data from a public API."})
@api.doc(params={"post": "The ID of the post to grab"}, responses={200: "Success", 400: "Missing parameters"})
class TestEndpointCall(Resource):
    def get(self):
        post_id = request.args.get('post')
        if post_id:
            PARAMS = { "postId": post_id }
            req = requests.get(url = "https://jsonplaceholder.typicode.com/comments", params = PARAMS)
            data = req.json()
            # Simply return the first instance
            test_post = data[0]
            return {"success": True, "data": test_post}
        else:
            return "Missing parameters", 400