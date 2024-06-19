from . import app_auth_bp


@app_auth_bp.route('/register', methods=['POST'])
def app_register():
    pass


@app_auth_bp.route('/login', methods=['POST'])
def app_login():
    pass

