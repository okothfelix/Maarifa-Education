from flask import render_template, request, redirect, url_for, session
import generators
from . import cbc_bp
import decorators
import cbc


@cbc_bp.route('/login', methods=['POST', 'GET'])
@decorators.user_login_checker
@decorators.handle_errors
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result_set = cbc.user_login(username, password)
        if result_set is None:
            return redirect(url_for('cbc.login'))
        return redirect(url_for('user_dashboard'))
    else:
        return render_template('cbc/login.html')


@cbc_bp.route('/user/dashboard', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def user_dashboard():
    cur_user = generators.cur_user_details(session['maarifa-education-id'])
    result_set = cbc.
    return render_template('user-dashboard.html', admin_name=cur_user[0], )
