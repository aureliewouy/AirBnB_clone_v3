#!/usr/bin/python3
""" Create URL routes Blueprint """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    """ Returns json status OK """
    return jsonify({"status": "OK"})

@app_views.route("/stats")
def stats():
    """ Returns the count method """
    """return storage.count()"""
