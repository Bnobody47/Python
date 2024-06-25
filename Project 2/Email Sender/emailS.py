import smtplib
from email.mime.text import MIMEText

to = input("Enter the email of recipent:\n")

content = input("Enter the content for mail:\n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'password')
    server.sendmail('your email', to, content)
    server.close()

sendEmail(to, content)