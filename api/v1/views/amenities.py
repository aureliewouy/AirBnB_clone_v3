#!/usr/bin/python3
"""
A new view for State objects that handles all default RestFul API actions
"""

from flask import Flask, abort, make_response, jsonify, request
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """retrieves the list of all Amenities objects with info about amenities"""
    amenities = []
    for amenity in storage.all(Amenity).values():
        amenities.append(amenity.to_dict())
    return jsonify(amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity_obj(amenity_id):
    """get info about state obj by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        return jsonify(amenity.to_dict())
    else:
        abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity_obj(amenity_id):
    """delete amenity obj by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        amenity.delete()
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity_obj():
    """creates a Amenity"""
    # request.get_json() - converts the JSON object into Python data
    state_data = request.get_json()
    if not amenity_data:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in amenity_data:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    # obj = class(**kwargs)
    amenity = Amenity(**amenity_data)
    amenity.save()
    return make_response(jsonify(amenity.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def put_amenity_obj(amenity_id):
    """update state obj by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, value in request.get_json().items():
        setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict())
