import smtplib
from email.message import EmailMessage

EMAIL_ID = "palindrome.innovations@gmail.com"
EMAIL_PASSWORD = "Black966!!!"


def sendMail(receiver_email, errorMessage):
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
