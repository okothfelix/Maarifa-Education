from . import frontend_bp
import decorators
from flask import render_template, request, session, redirect, url_for
import generators
import web_frontend
import secrets
import lower_learning_backend
import higher_learning_backend
import administrators_backend


@frontend_bp.route('/', methods=['POST', 'GET'])
@decorators.user_login_checker
@decorators.handle_errors
def index():
    return render_template('frontend/index.html')


@frontend_bp.route('/about', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def about():
    return render_template('frontend/about.html')


@frontend_bp.route('/analytics', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def analytics():
    return render_template('frontend/analytics.html')


@frontend_bp.route('/learning', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def learning():
    return render_template('frontend/learning.html')


@frontend_bp.route('/contacts', methods=['POST', 'GET'])
@decorators.user_login_checker
@decorators.handle_errors
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        number = request.form['phoneNumber']
        comment = request.form['message']
        web_frontend.user_contact_section(name, email, number, comment)
        session['contact-flag'] = True
        return redirect(url_for('contacts'))
    else:
        contact_flag = False
        if 'contact-flag' in session:
            contact_flag = True
            session.pop('contact-flag')
        return render_template('frontend/contacts.html', contact_flag=contact_flag)


@frontend_bp.route('/register', methods=['GET', 'POST'])
@decorators.user_login_checker
@decorators.handle_errors
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        number = generators.phone_num_checker(request.form['number'])
        if password != confirm_password:
            return redirect(url_for('frontend.error_log'))
        result_set = web_frontend.user_registration(username, email, password, number)
        if result_set:
            return redirect(url_for('frontend.account_activation'))
        elif result_set is False:
            return redirect(url_for('frontend.register'))
        return redirect(url_for('frontend.error_log'))
    else:
        return render_template('frontend/register.html')


@frontend_bp.route('/account-activation', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def account_activation():
    return render_template('frontend/account-activation.html')


@frontend_bp.route('/login', methods=['POST', 'GET'])
@decorators.user_login_checker
@decorators.handle_errors
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result_set = lower_learning_backend.user_login(username, password)
        if result_set:
            session['maarifa_education_id'] = maarifa_education_id = secrets.token_hex(10)
            sub_set = generators.session_update_section(maarifa_education_id, username, 1)
            if sub_set is None:
                return redirect(url_for('frontend.error_log'))
            session['logged_in'] = True
            return redirect(url_for('lower_learning.dashboard'))
        elif result_set is False:
            # check the higher learning database
            result_set = higher_learning_backend.admin_login(username, password)
            if result_set:
                session['maarifa_education_id'] = maarifa_education_id = secrets.token_hex(10)
                sub_set = generators.session_update_section(maarifa_education_id, username, 2)
                if sub_set is None:
                    return redirect(url_for('frontend.error_log'))
                session['logged_in'] = True
                return redirect(url_for('higher_learning.dashboard'))
            elif result_set is False:
                # check the administrators database
                result_set = administrators_backend.admin_login(username, password)
                if result_set:
                    session['maarifa_education_id'] = maarifa_education_id = secrets.token_hex(10)
                    sub_set = generators.session_update_section(maarifa_education_id, username, 3)
                    if sub_set is None:
                        return redirect(url_for('frontend.error_log'))
                    session['logged_in'] = True
                    return redirect(url_for('administrators.dashboard'))
                elif result_set is False:
                    return redirect(url_for('frontend.register'))
        return redirect(url_for('frontend.error_log'))
    else:
        register_flag = False
        if 'register-flag' in session:
            register_flag = True
        return render_template('frontend/login.html', register_flag=register_flag)


@frontend_bp.route('/password-recovery', methods=['GET', 'POST'])
@decorators.handle_errors
def forgot_password():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        result_set = web_frontend.user_forgot_password_section(email)
        if result_set:
            return render_template('account-activation.html')
        return redirect(url_for('frontend.error_log'))
    else:
        return render_template('frontend/forgot-pwd.html')


@frontend_bp.route('/update-password/<activation_code>', methods=['GET', 'POST'])
@decorators.handle_errors
def password_update(activation_code):
    cur_user = generators.cur_user_details(session['maarifa_education_id'])
    if request.method == "POST":
        new_password = request.form['new-password']
        confirm_password = request.form['confirm-password']
        if new_password != confirm_password:
            return redirect(url_for('password_update', activation_code=activation_code))

        result_set = web_frontend.password_update_section(activation_code, confirm_password)
        session['maarifa_education_id'] = maarifa_education_id = secrets.token_hex(10)
        sub_set = generators.session_update_section(maarifa_education_id, cur_user[1], result_set)
        if sub_set is not None:
            session['logged_in'] = True
            if result_set == 0:
                return redirect(url_for('users.user_dashboard'))
    else:
        result_set = web_frontend.activation_code_checker(activation_code)
        if result_set:
            return render_template('password-update.html')
    return redirect(url_for('error_log'))


@frontend_bp.route('/error', methods=['GET'])
def error_log():
    return render_template('frontend/404.html')
