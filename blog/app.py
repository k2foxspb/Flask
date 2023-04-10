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


@app.route('/user/')
def read_user():
    name = request.args.get('name')
    surname = request.args.get('surname')
    return f"User {name or '[no name]'} {surname or '[no surname]'}"


@app.route('/status/', methods=['GET', 'Post'])
def costum_status_code():
    if request.method == 'GET':
        return '''\
        To get response with custom status code
send request using POST method
and pass `code` in JSON body / FormData
'''
    print('raw bytes data:', request.data)

    if request.form and 'code' in request.form:
        return 'code from form', request.form['code']
    if request.json and "code" in request.json:
        return "code from json", request.json["code"]
    return "", 204


@app.before_request
def process_before_request():
    """Sets start_time to `g` object"""
    g.start_time = time()


@app.after_request
def process_after_request(response):
    """
    adds process time in headers
    """
    if hasattr(g, 'start_time'):
        response.headers['process_time'] = time() - g.start_time

    return response
