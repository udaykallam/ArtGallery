import smtplib

smtp_server = 'smtp.sendgrid.net'
smtp_port = 587
smtp_user = 'artgallery5656@gmail.com'
smtp_password = 'kdqs snjw jgcc xvju'

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.quit()
    print("SMTP Connection Successful")
except Exception as e:
    print(f"SMTP Error: {e}")
