#!/usr/bin/python3
"""
returns status: OK
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """returns status: OK"""
    status = {"status": "OK"}
    return jsonify(status)


@app_views.route('/stats')
def count():
    """ returns number of objects """
    total = {}
    classes = {"Amenity": "amenities",
               "City": "cities",
               "Place": "places",
               "Review": "reviews",
               "State": "states",
               "User": "users"}
    for cls in classes:
        count = storage.count(cls)
        total[classes.get(cls)] = count
    return jsonify(total)
