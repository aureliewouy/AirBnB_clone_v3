#!/usr/bin/python3
""" Create URL routes Blueprint """
from api.v1.views import app_views
from flask import jsonify
from models import storage

objs = {"amenities": "Amenity", "cities": "City", "places": "Place",
        "reviews": "Review", "states": "State", "users": "User"}


@app_views.route("/status")
def status():
    """ Returns json status OK """
    return jsonify({"status": "OK"})


@app_views.route("/api/v1/stats")
def stats():
    """ Returns the count method """
    dict_type = {}
    for key, value in objs.items():
        dict_type[key] = storage.count(value)
    return jsonify(dict_type)
