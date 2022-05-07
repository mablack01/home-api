import unittest
from flask import Flask
from flask_testing import LiveServerTestCase
from ..src import flask_app

class HomeAPITest(LiveServerTestCase):

    def create_app(self):
        app = flask_app()
        return app

    def test_server_is_up_and_running(self):
        response = self.client.get("/home/testing")
        self.assertEqual(response.code, 400)

if __name__ == '__main__':
    unittest.main()