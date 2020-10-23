import smtplib
from email.message import EmailMessage
import re
import time

print("Welcome to EmailSpammer! Login to your Email:")

# Regular expression to check email validity.
regex = '^[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
x = 1
emailTo = []  # List to store emails
getAgain = True
while getAgain is True:
    EmailAdd = input("Email: ")
    if re.search(regex, EmailAdd):
        getAgain = False
    else:
        print("Invalid Email. Please try again.")
        getAgain = True

Pass = input("Password: ")
getAgain = True
# Check email for validity and get multiple emails
while getAgain is True:
    getEmail = input("To: ")
    if (re.search(regex, getEmail)):
        emailTo.append(getEmail)
        getAgain = input("Do you want to add another email? Y/N ")
        if getAgain.lower() == "y":
            getAgain = True
        else:
            getAgain = False
    else:
        print("Invalid Email. Please try again.")
        getAgain = True

msg = EmailMessage()
msg['From'] = EmailAdd
msg['To'] = emailTo
msg['Subject'] = input("Subject: ")
msg.set_content(input("Content: "))
y = input("Number of times to send Email: ")
while x <= int(y):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        try:
            smtp.login(EmailAdd, Pass)
            smtp.send_message(msg)
        except:
            print("Sign in was blocked or Invalid Account. Make sure that you have ''Less secure apps'' enabled on your email.")
    print("Email Sent.")
    x += 1
