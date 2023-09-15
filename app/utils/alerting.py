"""
This module provides functions and mechanisms to send alerts or notifications. 

Use Cases:
-------------
If there's a critical error in the application, this module can be used to send an 
email or other types of alerts to the administrators.

Functions:
-------------
send_alert: Sends alerts/notfication with the given message. The current implementation is a placeholder.
You can integrate with services like Sentry, PagerDuty, or even send an email
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_alert(message, to_email, from_email, email_password, smtp_server, smtp_port):
    """
    Sends an alert with the given message via email.
    This function uses SMTP lib for sending email.

    Parameters
    ----------
    message : str
        The message for the alert.
    to_email: str
        The recipient's email address.
    from_email: str
        The sender's email address.
    email_password: str
        The senders's email password.
    smtp_server: str
        The smtp server for sending email.
    smtp_port: int
        The smtp server port for sending email.
    """
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Application Alert"

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, email_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()
