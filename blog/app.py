from time import time

from flask import Flask, request, g
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, Web!'


@app.route('/greet/<name>/')
def index(name: str):
    return f'Hello, {name}!'