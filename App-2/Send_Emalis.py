import smtplib, ssl

def Send_Emails(message):
    host = "smtp.gmail.com"
    port = 465

    username = "sharib@gmail.com"
    password = "your_password"

    receiver = "sharib@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(
            from_addr=username,
            to_addrs="receiver",
            msg="Subject: Test Email\n\nThis is a test email.")