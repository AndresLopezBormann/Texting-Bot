#This Project will help me cram a bit more python to prepare for EECS 268
from email import message
from re import sub
import smtplib, email, ssl
from email.message import EmailMessage
from providers import PROVIDERS

def EmailAlert(number:str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str = "Sent Using Python",
    smtp_server = "smtp.gmail.com",
    smtp_port: int = 465
    ):
        sender_email, email_password = sendercredentials
        receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

        email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

        with smtplib.SMTP_SSL(
            smtp_server, smtp_port, context=ssl.create_default_context()
        ) as email:
            email.login(sender_email, email_password)
            email.sendmail(sender_email,receiver_email, email_message)
def main():
    number = "9137027145"
    message = "Hello World"
    provider = "Sprint"
    sender_credentials = ("lpzandn@gmail.com,")
    EmailAlert()