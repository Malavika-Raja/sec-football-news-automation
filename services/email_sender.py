import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_ADDRESS,EMAIL_PASSWORD,RECIPIENT_EMAIL

def send_email(summary:str):
    """
    Sends weekly SEC football summary
    """

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = "Weekly SEC football news"

    body = f"""Hilloo,

Here goes your weekly football summary:

{summary}

With dedication,
Malu
"""
    msg.attach(MIMEText(body,"plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

    print("Email Sent Successfully")