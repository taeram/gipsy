from app import app, \
                cors_header
from flask import request, \
                  make_response, \
                  send_from_directory
import json
import os


@app.route('/.well-known/acme-challenge/<filename>')
def letsencrypt(filename):
    return send_from_directory(os.path.join(app.root_path, '../.well-known/acme-challenge/'), filename)


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
