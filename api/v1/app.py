#!/usr/bin/python3
""" Start flex app """

import os
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.register.blueprint(app_views)

@app.teardwon_appcontext
def close_db(error):
    """close storage"""
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    """Error handler"""
    return make_response(jsonify({"Error": "Not found"}), 404)

if __name__ == '__main__':
    # set the port and host
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000)
    # Run the flask server using thread=true
    app.run(host=host, port=port, threaded=True)
