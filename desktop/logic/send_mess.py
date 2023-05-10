import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_email(to_addr, body_text):
    """
    Send an email
    """
    host = 'smtp.mail.ru'
    port = 587
    username = 'adamova.01@mail.ru'
    password = 'vcdessZc1yJQy8kwtuEb'
    subject = 'Результаты последнего тестирования'
    from_addr = 'adamova.01@mail.ru'

    message = MIMEMultipart()
    message['From'] = from_addr
    message['To'] = to_addr
    message['Subject'] = Header(subject, 'utf-8')

    body = MIMEText(body_text, 'plain', 'utf-8')
    message.attach(body)

    try:
        server = smtplib.SMTP(host, port)
        server.starttls()
        server.login(username, password)
        server.sendmail(from_addr, to_addr, message.as_string())
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f'Email sending failed. Error message: {str(e)}')