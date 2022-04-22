import smtplib
from email.message import EmailMessage


def sendMail(receiver_email, errorMessage):
    from MailCreds import EMAIL_ID, EMAIL_PASSWORD

    msg = EmailMessage()
    msg.set_content(errorMessage)

    msg['Subject'] = 'Book Rating'
    msg['From'] = EMAIL_ID
    msg['To'] = receiver_email

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(EMAIL_ID, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()
