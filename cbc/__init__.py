from flask import Blueprint

cbc_bp = Blueprint('lower_learning', __name__)

from . import routes
