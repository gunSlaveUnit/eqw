import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class EmailSender:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, to_addr, body_text, subject):
        """
        Send an email
        """
        from_addr = self.username

        message = MIMEMultipart()
        message['From'] = from_addr
        message['To'] = to_addr
        message['Subject'] = Header(subject, 'utf-8')

        body = MIMEText(body_text, 'plain', 'utf-8')
        message.attach(body)

        try:
            server = smtplib.SMTP(self.host, self.port)
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(from_addr, to_addr, message.as_string())
            server.quit()
            print('Email sent successfully')
        except Exception as e:
            print(f'Email sending failed. Error message: {str(e)}')