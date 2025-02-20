import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

password = os.getenv("EMAIL_PASSWORD")

class Email:
    def __init__(self):
        self.from_email =  "maha.thamarai.m@gmail.com"  
        self.password = password
        self.to_email = "mahasel.1969@gmail.com" 
    
    def send_email(self):

        server = smtplib.SMTP("smtp.gmail.com: 587")
        server.starttls()
        server.login(self.from_email, self.password)
        message = MIMEMultipart()
        message["From"] = self.from_email
        message["To"] = self.to_email
        message["Subject"] = "Help"

        message_body = f"Emergency Needed!!"
        message.attach(MIMEText(message_body))

        try:
            server.send_message(message)
            print("✅ Email sent successfully!")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
