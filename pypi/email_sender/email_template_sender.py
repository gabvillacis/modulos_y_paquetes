
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.from_email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")

    def send(self, email):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.from_email, self.password)        
        
        mail = MIMEMultipart('alternative')
        mail['Subject'] = 'Calificación Módulos y Paquetes'
        mail['From'] = self.from_email
        mail['To'] = email

        html_template = """
        <h1>EELA - Curso de Python</h1>

        <p>Hola {0},</p>
        <p>Queremos anunciarte que has obtenido una calificación {1} (sobresaliente) en el curso y por ende aprobado.</p>            
        <p>Saludos<p>
        """

        html_content = MIMEText(html_template.format(email.split("@")[0], 19), 'html')            

        mail.attach(html_content)

        service.sendmail(self.from_email, email, mail.as_string())

        service.quit()


    def bulk_send(self, emails):
        for email in emails:
            self.send(email)


if __name__ == '__main__':
    recipients = input("Ingrese el(los) destinatario(s): ").split()
    
    mail = Mail()
    mail.bulk_send(recipients)