#!/usr/bin/python3
"""
Package Blueprint
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
<<<<<<< HEAD
from api.v1.views.places import *
=======
from api.v1.views.places_reviews import *
"""from api.v1.views.places import *"""
>>>>>>> 5fd2f3032ac7a62deccc60887f3cba7c0087823a
