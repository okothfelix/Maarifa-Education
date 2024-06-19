from flask import Blueprint

cbc_bp = Blueprint('higher_learning', __name__)

from . import routes
