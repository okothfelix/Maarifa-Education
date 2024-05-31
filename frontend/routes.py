from flask import render_template, request, session, redirect, url_for
from . import frontend_bp
import decorators
import web_frontend


@frontend_bp.route('/', methods=['POST', 'GET'])
# @decorators.user_login_checker
# @decorators.handle_errors
def index():
    return render_template('index.html')


@frontend_bp.route('/about', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def about():
    return render_template('about.html')


@frontend_bp.route('/analytics', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def analytics():
    return render_template('analytics.html')


@frontend_bp.route('/learning', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def learning():
    return render_template('learning.html')


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
        return render_template('contacts.html', contact_flag=contact_flag)


@frontend_bp.route('/error', methods=['GET'])
def error_log():
    return render_template('404.html')
