import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import africastalking


class Notifications:

    def __init__(self):
        # Set your app credentials
        self.username = "maarifa_edu"
        self.api_key = "e552051e33ce469b109fe81b87d81d42eb53c7bc4b6b2b1317245c18de529c07"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self, recipients, message):
        try:
            response = self.sms.send(message, recipients)
            return response
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))
            return e


con = Notifications()


def sender(phone_number, message):
    return con.send([phone_number], message)


def email_notification_section(send_to, activation_link, name, message='', flag=0):
    msg = MIMEMultipart()
    msg['From'] = 'accounts@beemultiscent.com'
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)

    if flag == 0:
        msg['Subject'] = "BEEMULTISCENT ACCOUNT REGISTRATION ACTIVATION."
        msg.attach(MIMEText("Dear " + name + ".\n\nYou are one step closer to finishing your account registration. Click the activation link below to complete registration.\n\n" + activation_link + "\n\nRegards.\nAccounts Team.\n"))
    elif flag == 1:
        msg['Subject'] = "BEEMULTISCENT ACCOUNT RECOVERY."
        msg.attach(MIMEText("Dear " + name + ".\n\nYou have requested for a password update. Click the activation link below to update your password.\n\n" + activation_link + "\n\nRegards.\nAccounts Team.\n"))
    elif flag == 2:
        msg['Subject'] = "BEEMULTISCENT AFFILIATE ACCOUNT REGISTRATION ACTIVATION."
        msg.attach(MIMEText("Dear " + name + ".\n\nYou have been registered as an affiliate for BeeMultiscent platform. If you did not request to be registered please ignore this message else click on the activation link below to update your account information.\n\n" + activation_link + "\n\nRegards.\nBeeMultiscent Operations.\n"))
    elif flag == 4:
        msg['Subject'] = "BEEMULTISCENT USER ACCOUNT ACTIVATION."
        msg.attach(MIMEText("Dear " + name + ".\n\nYou have been successfully registered as a user for BeeMultiscent. Click the activation link below to update your password and login to your account.\n\n" + activation_link + "\n\nDo not replay to this email.\n\nRegards.\nAccounts Team.\n"))
    else:
        msg['Subject'] = "BEEMULTISCENT CLIENT ENQUIRY"
        msg.attach(MIMEText(message))

    smtp = smtplib.SMTP_SSL('mail.beemultiscent.com', 465)
    smtp.ehlo()
    smtp.login('accounts@beemultiscent.com', 'p[6h@).ciu!T')
    smtp.sendmail('accounts@beemultiscent.com', send_to, msg.as_string())
    smtp.quit()
