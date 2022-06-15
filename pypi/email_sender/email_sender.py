
import smtplib, ssl
from dotenv import load_dotenv
import os

load_dotenv()

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.from_email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.from_email, self.password)
        
        for email in emails:
            service.sendmail(self.from_email, email, f"Subject: {subject}\n{content}")            

        service.quit()


if __name__ == '__main__':
    recipients = input("Ingrese el(los) destinatario(s): ").split()
    subject = input("Ingrese el asunto: ")
    content = input("Ingrese el mensaje: ")

    mail = Mail()
    mail.send(recipients, subject, content) 