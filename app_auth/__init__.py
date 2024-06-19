from flask import Blueprint

app_auth_bp = Blueprint('app_auth', __name__)

from . import routes
