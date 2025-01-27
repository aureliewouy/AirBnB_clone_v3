#!/usr/bin/python3
"""
A new view for Review objects that handles all default RestFul API actions
"""

from flask import Flask, abort, make_response, jsonify, request
from models import storage
from api.v1.views import app_views
from models.user import User
from models.place import Place
from models.review import Review


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_review(place_id):
    """retrieves the list of all Review objects with info about states"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = []
    for review in place.reviews:
        reviews.append(review.to_dict())
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_reviewobj(review_id):
    """retrieves a Review object"""
    review = storage.get(Review, review_id)
    if review:
        return jsonify(review.to_dict())
    else:
        abort(404)


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_reviewobj(review_id):
    """delete review obj by id"""
    review = storage.get(Review, review_id)
    if review:
        review.delete()
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_revieweobj(place_id):
    """creates a Review"""
    kwargs = request.get_json()
    if storage.get(Place, place_id) is None:
        abort(404)
    if storage.get(User, kwargs['user_id']) is None:
        abort(404)

    if not kwargs:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'user_id' not in kwargs:
        return make_response(jsonify({'error': 'Missing user_id'}), 400)
    if 'text' not in kwargs:
        return make_response(jsonify({'error': 'Missing text'}), 400)
    kwargs['place_id'] = place_id
    review = Review(**kwargs)
    review.save()
    return make_response(jsonify(review.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def put_reviewobj(review_id):
    """update review obj by id"""
    ignore_keys = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    kwargs = request.get_json()
    if not kwargs:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, value in kwargs.items():
        if key not in ignore_keys:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200
