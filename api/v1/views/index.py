#!/usr/bin/python3
"""
Index view module
"""

from api.v1.views import app_views
from flask import jsonify

# from api.v1.views.view1 import *


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Route to return a JSON status response
    """
    return jsonify({"status": "OK"})
