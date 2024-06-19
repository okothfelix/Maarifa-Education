from . import higher_learning_bp
import decorators
import generators
from flask import session, request
import sql_stmt
import payments


@higher_learning_bp.route('/purchase-sms', methods=['POST'])
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