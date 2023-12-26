from datetime import datetime
from flask import Flask, render_template, request, make_response, jsonify
import requests

app = Flask(__name__, instance_relative_config=True)

LOG_URL = 'http://log-service:3000'

def log_operation(operation, a, b, result):
    # Log the operation
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'service': 'math',
        'operation': operation,
        'arguments': {'a': a, 'b': b},
        'result': result
    }
    requests.post(LOG_URL + '/addLog', json=log_entry)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        result = a + b
        log_operation('add', a, b, result)
        return make_response(jsonify(s=a+b), 200) # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) # HTTP 400 BAD REQUEST

#add other routes here

@app.route('/sub')
def sub():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    
    if a and b:
        result = a - b
        log_operation('sub', a, b, result)
        return make_response(jsonify(s=a-b), 200)
    else:
        return make_response('Invalud input\n', 400)

@app.route('/mul')
def mul():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    
    if a and b:
        result = a * b
        log_operation('mul', a, b, result)
        return make_response(jsonify(s=a*b), 200)
    else:
        return make_response('Invalud input\n', 400)
    
@app.route('/div')
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    
    if a and b:
        result = a / b
        log_operation('div', a, b, result)
        return make_response(jsonify(s=a/b), 200)
    else:
        return make_response('Invalud input\n', 400)
    
@app.route('/mod')
def mod():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    
    if a and b:
        result = a % b
        log_operation('mod', a, b, result)
        return make_response(jsonify(s=a%b), 200)
    else:
        return make_response('Invalud input\n', 400)

def create_app():
    return app