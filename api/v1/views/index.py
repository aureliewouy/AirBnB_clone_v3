#!/usr/bin/python3
""" Create URL routes Blueprint """
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage

# objs = {"amenities": "Amenity", "cities": "City", "places": "Place",
#        "reviews": "Review", "states": "State", "users": "User"}


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Returns json status OK """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ Returns the count method """
#   dict_type = {}
#   for key, value in objs.items():
#       dict_type[key] = storage.count(value)
    return jsonify({"amenities": storage.count('Amenity'),
                    "cities": storage.count('City'),
                    "places": storage.count('Place'),
                    "reviews": storage.count('Review'),
                    "states": storage.count('State'),
                    "users": storage.count('User')})
