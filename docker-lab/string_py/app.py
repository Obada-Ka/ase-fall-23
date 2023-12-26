from datetime import datetime
from flask import Flask, render_template, request, make_response, jsonify
import requests

app = Flask(__name__, instance_relative_config=True)

LOG_URL = 'http://log-service:3000'

def log_operation(operation, a, b, result):
    # Log the operation
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'service': 'string',
        'operation': operation,
        'arguments': {'a': a, 'b': b},
        'result': result
    }
    requests.post(LOG_URL + '/addLog', json=log_entry)
    
@app.route('/concat')
def concat():
    a = request.args.get('a', type=str)
    b = request.args.get('b', type=str)
    if a and b:
        result = a + b
        log_operation('concat', a, b, result)
        return make_response(jsonify(s=a+b), 200) # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) # HTTP 400 BAD REQUEST

@app.route('/upper')
def upper():
    a = request.args.get('a', 0, type=str)
    result = a.upper()
    log_operation('upper', a, 0, result)
    return make_response(jsonify(s=a.upper()), 200)

@app.route('/lower')
def mul():
    a = request.args.get('a', 0, type=str)
    result = a.lower()
    log_operation('lower', a, 0, result)
    return make_response(jsonify(s=a.lower()), 200)


def create_app():
    return app