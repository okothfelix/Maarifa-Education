import secrets
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


def user_registration(username, email, password, number):
    conn = generators.connect_to_mysql()
    c = conn.cursor(buffered=True)
    # checking for 1062 error
    try:
        c.execute(sql_stmt.user_register_1.format(address=email))
        user_id = c.fetchone()[0]
        conn.close()
        return False
    except TypeError:
        pass
    except Exception as e:
        if str(e)[:str(e).find(" ")] == "1146":
            pass
        else:
            print(e)
            conn.close()
            return
    cur_day = generators.cur_day_generator()
    c.execute(sql_stmt.user_login_2.format(password=password))
    p_word = c.fetchone()[0]
    try:
        c.execute(sql_stmt.user_register_2.format(username=username, email=email, number=number, password=p_word,
                                                  date_created=cur_day, last_updated=cur_day))
    except Exception as e:
        if str(e)[:str(e).find(" ")] == "1146":
            c.execute(sql_stmt.user_register_3)
            c.execute(sql_stmt.user_register_2.format(username=username, email=email, number=number, password=p_word,
                                                      date_created=cur_day, last_updated=cur_day))
        else:
            print(e)
            conn.close()
            return

    # add the activation code
    while True:
        activation_code = secrets.token_hex(32)
        try:
            c.execute(sql_stmt.activation_1.format(activation_code=activation_code[:20]))
            result_set = c.fetchone()[0]
        except TypeError:
            c.execute(sql_stmt.activation_3.format(user_type=0, activation_code=activation_code[:20], address=email,
                                                   date_created=cur_day))
        except Exception as e:
            if str(e)[:str(e).find(" ")] == "1146":
                c.execute(sql_stmt.activation_2)
                c.execute(sql_stmt.activation_3.format(user_type=0, activation_code=activation_code[:20], address=email,
                                                       date_created=cur_day))
            else:
                print(e)
                conn.close()
                return
        break
    conn.commit()
    conn.close()

    # send the account activation email to the user
    thread_obj = threading.Thread(target=email_notification_section, args=[])
    thread_obj.start()


def user_forgot_password_section(email):
    pass
