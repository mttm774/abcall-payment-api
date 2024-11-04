from flask_restful import Resource, Api
from flask import Flask, request, json
from .utils.json_custom_encoder import JSONCustomEncoder
import requests
from flaskr import create_app
from config import Config
from .endpoint import HealthCheck, Invoices
import signal
import logging
from flask_cors import CORS

config = Config()


app = create_app()
CORS(app)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('default')
app.json_encoder = JSONCustomEncoder

def before_server_stop(*args, **kwargs):
    logger.info('Closing application ...')

signal.signal(signal.SIGTERM, before_server_stop)

app_context = app.app_context()
app_context.push()



api = Api(app)

#resources
api.add_resource(HealthCheck, '/health')
api.add_resource(Invoices, '/invoices/<string:action>',endpoint='invoices')
api.add_resource(Invoices, '/GenerateInvoice/<string:action>',endpoint='post_operations')