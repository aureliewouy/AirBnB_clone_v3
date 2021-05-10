#!/usr/bin/python3
"""
Package Blueprint
"""
from api.v1.views.index import *
from api.v1.views.states import *
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
