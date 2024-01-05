import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_dynamic_email(sender_email, sender_password, recipient_email, subject, body):
    

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  
        server.login(sender_email, sender_password)
        server.send_message(msg)


sender_email = "your_email@gmail.com"
sender_password = "your_password"
recipient_email = "
