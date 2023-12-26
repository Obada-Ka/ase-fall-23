import requests

from flask import Flask, jsonify, render_template, request, make_response
from requests.exceptions import ConnectionError, HTTPError
from urls import *

ALLOWED_MATH_OPS = ['add', 'sub', 'mul', 'div', 'mod']
ALLOWED_STR_OPS = ['lower', 'upper', 'concat', 'editdistance']

app = Flask(__name__, instance_relative_config=True)

LOG_URL = 'http://log-service:3000'

def get_logs_from_service():
    try:
        response = requests.get(LOG_URL + '/getLog')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return []
    except requests.exceptions.HTTPError:
        return []

@app.route('/math/<op>')
def math(op):
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if op not in ALLOWED_MATH_OPS:
        return make_response('Invalid new math operation\n', 404)
    try:
        x = requests.get(MATH_URL + f'/{op}?a={a}&b={b}')
        x.raise_for_status()
        return x.json()
    except ConnectionError:
        return make_response('Math service is down\n', 404)
    except HTTPError:
        return make_response('Invalid input\n', 400)


@app.route('/str/<op>')
def string(op):
    a = request.args.get('a', type=str)
    b = request.args.get('b', type=str)
    if op not in ALLOWED_STR_OPS:
        return make_response('Invalid new string operation\n', 404)
    try:
        if op == 'lower' or op == 'upper':
            x = requests.get(STRING_URL + f'/{op}?a={a}')
        else:
            x = requests.get(STRING_URL + f'/{op}?a={a}&b={b}')
        x.raise_for_status()
        return x.json()
    except ConnectionError:
        return make_response('String service is down\n', 404)
    except HTTPError:
        return make_response('Invalid input\n', 400)

@app.route('/getLog')
def get_log():
    try:
        # Retrieve logs directly from the log service
        all_logs = get_logs_from_service()
        return jsonify(all_logs)
    except requests.exceptions.ConnectionError:
        return make_response('Log service is down\n', 404)
    except requests.exceptions.HTTPError:
        return make_response('Error retrieving logs\n', 500)

def create_app():
    return app
