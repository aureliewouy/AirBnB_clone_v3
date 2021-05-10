#!/usr/bin/python3
"""
A new view for Review objects that handles all default RestFul API actions
"""

from flask import Flask, abort, make_response, jsonify, request
from models import storage
from api.v1.views import app_views
from models.place import Place
from models.review import Review


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_review(place_id):
    """retrieves the list of all Review objects with info about states"""
    reviews = []
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    for review in storage.all(Review).values():
        if place_id == review.to_dict()['place_id']:
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
def create_revieweobj():
    """creates a Review"""
    place = storage.get(Place, place_id)
    user = storage.get(User, user_id)
    if place or user is None:
        abort(404)

    kwargs = request.get_json()
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
    for key, value in request.get_json().items():
        if key not in ignore_keys:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict())
