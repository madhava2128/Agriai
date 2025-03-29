from flask import Blueprint

# Create a blueprint for the routes
routes_bp = Blueprint('routes', __name__)

# Import the routes to register them with the blueprint
from .api import *
from .translations import *