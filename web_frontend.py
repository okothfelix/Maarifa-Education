import threading
from notifications import email_notification_section


def user_contact_section(name, address, number, message):
    mail = name + ".\n\n" + address + ".\n\n" + number + ".\n\n" + message + ".\n"
    send_to = 'okothfelix85@gmail.com'
    thread_obj = threading.Thread(target=email_notification_section, args=[send_to, '', '', mail, 2])
    thread_obj.start()
    return True
