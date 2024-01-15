#!/usr/bin/python3
"""
Initialize the views package
"""

from flask import Blueprint

# Create the Blueprint instance
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import your specific views using the Blueprint instance
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
# Import your specific views
# from api.v1.views.view1 import *
# from api.v1.views.view2 import *
# from api.v1.views.view3 import *
