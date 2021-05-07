#!/usr/bin/python3
""" Creates an url route for blueprint """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    """ Returns json status OK """
    return jsonify({"status": "OK"})

@app_views.route("/stats")
def status():
    """ Returns json status OK """
    return storage.count()
