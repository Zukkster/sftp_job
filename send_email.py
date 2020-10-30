import smtplib
import ssl
import os

print(os.environ['DB_DEV_PASSWORD'])

smtp_server = "smtp.gmail.com"
port = 465  # F0r starttls
sender_email = "db_dev@jin-analytics.co.uk"
receiver_email = "stuartkirkup@gmail.com"
password = os.environ['DB_DEV_PASSWORD']

message = """\
Subject: Hi there

This message is sent from Google Cloud"""

# Try to log in to server and send email
try:
    #server = smtplib.SMTP(smtp_server,port)
    #server.ehlo() # Can be omitted
    # server.starttls(context=context) # Secure the connection
    # server.ehlo() # Can be omitted
    # server.login(sender_email, password)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

except Exception as e:
    # Print any error messages to stdout
    print(e)
#finally:
    #server.quit()
