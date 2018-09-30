from flask import Flask, request, abort
app = Flask(__name__)

token = 'a-very-real-token'

@app.route('/login', methods = ['POST'])
def login():
    return token

@app.route('/')
def hello():
    token = request.headers.get('Authorization')
    if token != token:
        abort(401)
    print(f'Found token {token}')
    return 'Hello Locust!'
