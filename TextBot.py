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
        sender_email, email_password = sender_credentials
        receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

        email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

        with smtplib.SMTP_SSL(
            smtp_server, smtp_port, context=ssl.create_default_context()
        ) as email:
            email.login(sender_email, email_password)
            email.sendmail(sender_email,receiver_email, email_message)
def main():
    #Chenge Number and provider to the one you are trying to send to 
    number = "Number"
    message = "Hello World (Sprint)"
    provider = "provider"#Provider placed Here as a string



    #Change the Username and password to an Email and Password you want ot send this to
    #Note** You must activate IMAP and Allow Less secure access
    #IMAP: https://support.google.com/mail/answer/7126229?p=BadCredentials&visit_id=637781219190590327-2642252345&rd=2#cantsignin&zippy=%2Ci-cant-sign-in-to-my-email-client%2Cstep-change-smtp-other-settings-in-your-email-client%2Cstep-check-that-imap-is-turned-on
    #Less Secure: https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
    sender_credentials = ("UserName","Password")
    EmailAlert(number,message,provider,sender_credentials)

if __name__ == "__main__":
    main()