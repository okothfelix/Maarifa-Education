from flask import Blueprint

cbc_bp = Blueprint('cbc', __name__)

from . import routes
