from app import app
from flask import request
import json

@app.route('/', methods=['GET'])
def index():
    if 'X-Forwarded-For' in request.headers:
        ipAddress = request.headers['X-Forwarded-For']
    else:
        ipAddress = request.remote_addr

    response = json.dumps({
        "address": ipAddress
    })

    return app.response_class(response=response, mimetype='application/json')
