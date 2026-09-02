import smtplib
import ssl 

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "sharib2510@gmail.com"
    password = "weey ynca inyn uttq"
    
    receiver = "mohammedsharib2006@gmail.com"
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
