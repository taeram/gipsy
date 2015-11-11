from app import app, \
                cors_header
from flask import request, \
                  make_response
import json


@app.route('/', methods=['GET'])
@cors_header
def index():
    if 'X-Forwarded-For' in request.headers:
        ipAddress = request.headers['X-Forwarded-For']
    else:
        ipAddress = request.remote_addr

    response = json.dumps({
        "address": ipAddress
    })

    return app.response_class(response=response, mimetype='application/json')
