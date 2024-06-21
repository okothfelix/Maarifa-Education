import threading
import sql_stmt
import generators
from notifications import email_notification_section


def user_contact_section(name, address, number, message):
    mail = name + ".\n\n" + address + ".\n\n" + number + ".\n\n" + message + ".\n"
    send_to = 'okothfelix85@gmail.com'
    thread_obj = threading.Thread(target=email_notification_section, args=[send_to, '', '', mail, 2])
    thread_obj.start()
    return True


def user_registration(username, institution_name, level, email, number):
    # register the users institution for a pilot program
    try:
        generators.execute_sql(sql_stmt.user_pilot_register_1.format(username=username, institution_name=institution_name, level=level, email=email, number=number, date_created=generators.cur_day_generator()), commit_flag=True)
    except Exception as e:
        if str(e)[:str(e).find(" ")] == "1146":
            generators.execute_sql(sql_stmt.user_pilot_register_2, commit_flag=True)
            generators.execute_sql(sql_stmt.user_pilot_register_1.format(username=username, institution_name=institution_name, level=level, email=email, number=number, date_created=generators.cur_day_generator()), commit_flag=True)
        elif str(e)[:str(e).find(" ")] == "1062":
            return True
        else:
            return
    return True


def user_forgot_password_section(email):
    pass
