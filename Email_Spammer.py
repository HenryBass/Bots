import smtplib
from email.message import EmailMessage

print("Welcome to EmailSpammer! Login to your Email:")
EmailAdd = input("Email: ")
Pass = input("Password: ")

x = 1

msg = EmailMessage()
msg['From'] = EmailAdd
msg['To'] = input("To: ")
msg['Subject'] = input("Subject: ")
msg.set_content(input("Content: "))
y = input("Number of times to send Email: ")
while x <= int(y):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EmailAdd, Pass)
        smtp.send_message(msg)
    print("Email Sent.")
    x = x + 1
