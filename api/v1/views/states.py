#!/usr/bin/python3
"""
A new view for State objects that handles all default RestFul API actions
"""

from flask import Flask, abort, make_response, jsonify, request
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """retrieves the list of all State objects with info about states"""
    states = []
    for state in storage.all(State).values():
        states.append(state.to_dict())
    return jsonify(states)


@app_views.route('/states/<state_id>', methods=['GET'],
                 strict_slashes=False)
def get_stateobj(state_id):
    """get info about state obj by id"""
    state = storage.get(State, state_id)
    if state:
        return jsonify(state.to_dict())
    else:
        abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_stateobj(state_id):
    """delete state obj by id"""
    state = storage.get(State, state_id)
    if state:
        state.delete()
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_stateobj():
    """creates a State"""
    # request.get_json() - converts the JSON object into Python data
    kwargs = request.get_json()
    if not kwargs:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in kwargs:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    # obj = class(**kwargs)
    state = State(**kwargs)
    state.save()
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def put_stateobj(state_id):
    """update state obj by id"""
    ignore_keys = ['id', 'created_at', 'updated_at']
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    kwargs = request.get_json()
    if not kwargs:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, value in request.get_json().items():
        if key not in ignore_keys:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())
