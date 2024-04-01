#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>', 200

@app.route('/print/<string:parameter>')
def print_route(parameter):
    print (parameter)
    return parameter, 200

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ''
    for num in range (parameter):
        result += str(num) + '\n'
    return result, 200

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = str(num1+num2)
    elif operation == '-':
        result = str(num1-num2)
    elif operation == '*':
        result = str(num1*num2)
    elif operation == 'div':
        result = str(num1/num2)
    elif operation == '%':
        result = str(num1%num2)
    return result, 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
