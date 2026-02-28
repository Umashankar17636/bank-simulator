import smtplib
from email.message import EmailMessage

EMAIL = "..........."          # your Gmail ID
APP_PASSWORD = "............."  # your Gmail App Password

def send_mail(to, subject, text):
    msg = EmailMessage()
    msg.set_content(text)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, APP_PASSWORD)
            server.send_message(msg)
        print("✅ Mail sent successfully")

    except Exception as e:
        print("❌ Mail sending failed")
        print(e)


def openacn_mail(to, text):
    send_mail(to, "Account Opened in ABC Bank", text)


def closeotp_mail(to, text):
    send_mail(to, "OTP to Close Account", text)


def forgototp_mail(to, text):

    send_mail(to, "OTP to Recover Password", text)
