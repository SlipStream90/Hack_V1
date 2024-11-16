import smtplib
from email.message import EmailMessage
from config import EMAIL_CONFIG

def send_mail(name,email,message):
    with smtplib.SMTP_SSL(EMAIL_CONFIG["SMTP_SERVER"], EMAIL_CONFIG["PORT"]) as smtp:
        smtp.login(EMAIL_CONFIG["MAIL_ADDRESS"], EMAIL_CONFIG["MAIL_APP_PW"])
        msg = EmailMessage()
        msg.set_content(message)
        msg['subject'] = "Query Mail"
        msg['to'] = ""
        msg['from'] = EMAIL_CONFIG["MAIL_ADDRESS"]
        smtp.send_message(msg)
