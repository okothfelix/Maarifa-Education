from flask import render_template, request, redirect, url_for, session
import generators
import sql_stmt
from . import cbc_bp
import decorators
import lower_learning_backend
import payments


@cbc_bp.route('/user/dashboard', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def user_dashboard():
    cur_user = generators.cur_user_details(session['maarifa-education-id'])
    return render_template('lower_learning/user-dashboard.html', admin_name=cur_user[0], )


@cbc_bp.route('/user/profile', methods=['GET', 'POST'])
@decorators.admin_login_checker
@decorators.handle_errors
def user_profile():
    cur_user = generators.cur_user_details(session['maarifa_education_id'])
    if request.method == 'POST':
        f_name = request.form['first-name']
        l_name = request.form['last-name']
        email = request.form['address']
        number = request.form['phone-number']
        result_set = cbc_backend.user_profile_section('POST', cur_user[2], f_name, l_name, email, number)
        if result_set:
            session['update-flag'] = True
            return redirect(url_for('lower_learning.user_profile'))
        return redirect(url_for('frontend.error_log'))
    else:
        result_set = cbc_backend.user_profile_section('GET', cur_user[2])
        update_flag = False
        if 'update-flag' in session:
            update_flag = session['update-flag']
            session.pop('update-flag')
        return render_template('lower_learning/profile.html', admin_name=cur_user[0], admin_details=result_set, update_flag=update_flag)


@cbc_bp.route('/user/profile-password-update', methods=['POST'])
@decorators.admin_login_checker
@decorators.handle_errors
def user_profile_password_update_section():
    old_password = request.form['old-password']
    new_password = request.form['new-password']
    confirm_password = request.form['confirm-password']

    if new_password != confirm_password:
        return redirect(url_for('error_log'))
    cur_user = generators.cur_user_details(session['maarifa_education_id'])
    result_set = cbc_backend.update_user_password_section(cur_user[2], old_password, new_password)
    if result_set:
        session['update-password-flag'] = True
        return redirect(url_for('lower_learning.user_profile'))
    elif result_set is False:
        session['update-password-flag'] = False
        return redirect(url_for('lower_learning.user_profile'))
    else:
        return redirect(url_for('frontend.error_log'))


@cbc_bp.route('/user/purchase-sms', methods=['POST'])
@decorators.admin_login_checker
@decorators.handle_errors
def user_purchase_sms():
    agent = request.form['agent']
    amount = request.form['amount']
    phone_number = request.form['number']
    # initiate a c2b transaction
    sms_purchase = payments.c2b_payments(agent, amount, phone_number)
    if sms_purchase:
        cur_user = generators.cur_user_details(session['maarifa_education_id'])
        available_sms = generators.execute_sql(sql_stmt.lower_sms.format(i_d=cur_user[2]), result_flag=True)[1][0][0]
        # update the lower_learning user sms type.
        result_set = generators.execute_sql(sql_stmt.lower_sms_update.format(available_sms=available_sms+int(amount), i_d=cur_user[2]), commit_flag=True)[0]
        if result_set:
            # check if the available admin sms exceeds the purchased sms
            admin_available_sms = generators.execute_sql(sql_stmt.admin_sms, result_flag=True)[1][0][0]
            if admin_available_sms > available_sms:
                return True
            else:
                pass
    return False
