import unittest
from unittest.mock import patch
from flask import Flask
from flask_restful import Api
from http import HTTPStatus
from flaskr.endpoint.healthCheck.HealthCheck import HealthCheck

class TestHealthCheck(unittest.TestCase):

    def setUp(self):

        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(HealthCheck, '/healthcheck')
        self.client = self.app.test_client()  

    @patch('flaskr.endpoint.healthCheck.HealthCheck.Config')
    def test_get_healthcheck(self, mock_config):

        mock_config.ENVIRONMENT = "development"
        mock_config.APP_NAME = "TestApp"


        response = self.client.get('/healthcheck')


        self.assertEqual(response.status_code, HTTPStatus.OK)


