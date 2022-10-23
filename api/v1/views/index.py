#!/usr/bin/python3
"""
returns "status": "OK"
"""
from flask import jsonify
from app_views import api.v1.views


@app_views.route('/status')
def status():
    """returns "status": "OK""""
    status = {"status": "OK"}
    return jsonify(status)
