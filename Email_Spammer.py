import smtplib
from email.message import EmailMessage
import re

print("Welcome to EmailSpammer! Login to your Email:")
EmailAdd = input("Email: ")
Pass = input("Password: ")

#Regular expression to check email validity.
regex = '^[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
x = 1
emailTo = [] #List to store emails
getAgain = True 

#Check email for validity and get multiple emails
while getAgain is True:
    getEmail = input("To: ")
    if(re.search(regex, getEmail)):
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
        smtp.login(EmailAdd, Pass)
        smtp.send_message(msg)
    print("Email Sent.")
    x = x + 1
