from flask import render_template, request, session, redirect, url_for
import decorators
import generators
from . import frontend_bp
import decorators
import web_frontend


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


@frontend_bp.routes('/register', methods=['GET', 'POST'])
@decorators.user_login_checker
@decorators.handle_errors
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        number = generators.phone_num_checker(request.form['number'])
        web_frontend.user_registration(username, email, password, confirm_password, number)
        return redirect(url_for('frontend.account_activation'))
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
        pass
    else:
        return render_template('frontend/login.html')


@frontend_bp.route('/error', methods=['GET'])
def error_log():
    return render_template('frontend/404.html')
