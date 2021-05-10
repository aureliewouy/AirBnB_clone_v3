#!/usr/bin/python3
"""
A new view for City objects that handles all default RestFul API actions
"""

from flask import Flask, abort, make_response, jsonify, request
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id):
    """retrieves the list of all City objects of a State"""
    cities = []
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    for city in storage.all(City).values():
        # verif state_id in json
        if state_id == city.to_dict()['state_id']:
            cities.append(city.to_dict())
    return jsonify(cities)


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_cityobj(city_id):
    """retrieves a City object"""
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    else:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_cityobj(city_id):
    """delete city obj by id"""
    city = storage.get(State, state_id)
    if city:
        city.delete()
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_cityobj():
    """creates a City"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    # request.get_json() - converts the JSON object into Python data
    city_data = request.get_json()
    if not city_data:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in city_data:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    # obj = class(**kwargs)
    city = City(**city_data)
    city.save()
    return make_response(jsonify(city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'],
                 strict_slashes=False)
def put_cityobj(state_id):
    """update city obj by id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, value in request.get_json().items():
        setattr(city, key, value)
    state.save()
    return jsonify(city.to_dict()), 200