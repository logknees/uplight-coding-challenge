from flask import render_template, request, jsonify, Response
from app import app 
import hmac
import json
import hashlib

@app.route('/')
def home():
    return "Hello! The container is running! Yippee!"

@app.route('/token', methods=['POST', 'GET'])
def token():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        obj = {}
        print('data', request.data)
        print('form', request.form)
        if request.data:
            obj = json.loads(request.data)
        elif request.form:
            obj = request.form.to_dict()
        else:
            return Response(
                "Bad request. Nothing in payload.",
                status=400,
            )
        obj['signature'] = generate_token(obj)
        return jsonify(obj)


def generate_token(request_dict):
    secret_key = b"NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
    encoded = json.dumps(request_dict, separators=(',', ':')).encode('ASCII')
    signature = hmac.new(secret_key, encoded, hashlib.sha256).hexdigest()

    return format(signature)