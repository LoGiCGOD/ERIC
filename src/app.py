# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return f'The sum of {num1} and {num2} is {result}.'

if __name__ == '__main__':
    app.run(debug=True)
