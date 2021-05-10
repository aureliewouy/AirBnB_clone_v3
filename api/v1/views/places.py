#!/usr/bin/python3
"""
A new view for State objects that handles all default RestFul API actions
"""

from flask import Flask, abort, make_response, jsonify, request
from models import storage
from api.v1.views import app_views
from models.place import Place
from models.city import City


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_city_by_place(city_id):
    """retrieves the list of all State objects with info about states"""
    city = storage.get(City, city_id)
    if city:
        places = []
        for place in city.places:
            places.append(place.to_dict())
        return jsonify(places)
    else:
        abort(404)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place(place_id):
    """get info about place obj by id"""
    place = storage.get(Place, place_id)
    if place:
        return jsonify(place.to_dict())
    else:
        abort(404)
"""
@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    delete place obj by id
    place = storage.get(Place, place_id)
    if place:
        place.delete()
        place.save()
        return jsonify({}), 200
    else:
        abort(404)

@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_placesobj(city_id):
    creates a State
    # request.get_json() - converts the JSON object into Python data
    kwargs = request.get_json()
    if not kwargs:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'user_id' not in kwargs:
        return make_response(jsonify({'error': 'Missing user_id'}), 400)
    if storage.get(User, kwargs["user_id"]) is None:
        abort(404)
    if storage.get("name") is None:
        return "Missing name", 400
    # obj = class(**kwargs)
    place = Place()
    for k, v in kwargs.items():
        setattr(place, k, v)
    setattr(place, "city_id", city_id)
    place.save()
    return jsonify(jsonify(place.to_dict()), 201

@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def put_placeobj(place_id):
    update place obj by id
    ignore_keys = ['id', 'created_at', 'updated_at', 'city_id', 'user_id']
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    kwargs = request.get_json()
    if not kwargs:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, value in request.get_json().items():
        if key not in ignore_keys:
            setattr(place, key, value)
    place.save()
    return jsonify(state.to_dict())
"""
