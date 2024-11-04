from flask import Flask
from datetime import timedelta


def create_app():
    app = Flask(__name__)
    return app

from .app import *