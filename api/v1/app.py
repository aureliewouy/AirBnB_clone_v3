#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """A method calls storage.close()"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """ set the 404 status explicitly"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST') or '0.0.0.0',
            port=os.getenv('HBNB_API_PORT') or '5000'
            , threaded=True)
