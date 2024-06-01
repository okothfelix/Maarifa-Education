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
    c.execute(sql_stmt.user_login_2.format(password=password))
    cur_day = generators.cur_day_generator()
    try:
        c.execute(sql_stmt)
    except Exception as e:
        if str(e)[:str(e).find(" ")] == "1146":
            c.execute("Create table Maarifa_Edu_Users (user_id int not null primary key auto_increment, username varchar(30) not null, address")
    conn.close()


def user_forgot_password_section(email):
    pass