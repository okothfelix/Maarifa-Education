from flask import Blueprint

administrators_bp = Blueprint('administrators', __name__)

from . import routes
