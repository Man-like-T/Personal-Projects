from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'ayotunde739@gmail.com'
email_pass = ''

email_receiver = 'cejeje4205@canyona.com'

subject = "Email With Python"
body = """
This is a test to send an email using pyhton.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_pass)
    smtp.sendmail(email_sender, email_receiver, em.as_string())