#!/usr/bin/python3
"""
A new view for User object that handles all default RestFul API actions
"""

from flask import Flask, abort, make_response, jsonify, request
from models import storage
from api.v1.views import app_views
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """retrieves the list of all User objects with users info"""
    users = []
    for user in storage.all(User).values():
        users.append(user.to_dict())
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_userobj(user_id):
    """get info about user obj by id"""
    user = storage.get(User, user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_userobj(user_id):
    """delete user obj by id"""
    user = storage.get(User, user_id)
    if user:
        user.delete()
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_userobj():
    """creates a User"""
    # request.get_json() - converts the JSON object into Python data
    kwargs = request.get_json()
    if not kwargs:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'email' not in kwargs:
        return make_response(jsonify({'error': 'Missing email'}), 400)
    if 'password' not in kwargs:
        return make_response(jsonify({'error': 'Missing password'}), 400)
    user = User(**kwargs)
    user.save()
    return make_response(jsonify(user.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def put_userobj(user_id):
    """update user obj by id"""
    ignore_keys = ['id', 'email', 'created_at', 'updated_at']
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, value in request.get_json().items():
        if key not in ignore_keys:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200
