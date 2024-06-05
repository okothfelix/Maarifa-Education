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
    return render_template('user-dashboard.html', admin_name=cur_user[0], )


@cbc_bp.route('/user/profile', methods=['GET', 'POST'])
@decorators.admin_login_checker
@decorators.handle_errors
def user_profile():
    cur_user = generators.cur_user_details(session['bms_id'])
    if request.method == 'POST':
        f_name = request.form['first-name']
        l_name = request.form['last-name']
        email = request.form['address']
        number = request.form['phone-number']
        result_set = cbc.user_profile_section('POST', cur_user[2], f_name, l_name, email, number)
        if result_set:
            session['update-flag'] = True
            return redirect(url_for('user_profile'))
        return redirect(url_for('error_log'))
    else:
        result_set = cbc.user_profile_section('GET', cur_user[2])
        update_flag = False
        if 'update-flag' in session:
            update_flag = session['update-flag']
            session.pop('update-flag')
        return render_template('user-profile.html', admin_name=cur_user[0], admin_details=result_set,
                               update_flag=update_flag)


@cbc_bp.route('/user/profile-password-update', methods=['POST'])
@decorators.admin_login_checker
@decorators.handle_errors
def user_profile_password_update_section():
    old_password = request.form['old-password']
    new_password = request.form['new-password']
    confirm_password = request.form['confirm-password']

    if new_password != confirm_password:
        return redirect(url_for('error_log'))
    cur_user = generators.cur_user_details(session['bms_id'])
    result_set = cbc.update_user_password_section(cur_user[2], old_password, new_password)
    if result_set:
        session['update-password-flag'] = True
        return redirect(url_for('user_profile'))
    elif result_set is False:
        session['update-password-flag'] = False
        return redirect(url_for('user_profile'))
    else:
        return redirect(url_for('error_log'))
