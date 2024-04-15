import smtplib
import os
import sys
from email.message import EmailMessage

EMAIL_RECIPIENT = os.environ['EMAIL_RECIPIENT']
OUTPUTFILE = "hello.txt"

with open(OUTPUTFILE, "w") as file:
    file.write("Hello World from trispera GitHub repo!")

msg = EmailMessage()
msg["From"] = "noreply@csc.fi"
msg["Subject"] = "Broken links report"
msg["To"] = os.getenv('EMAIL_RECIPIENT')
msg.set_content("You will find attached the broken links report of docs.csc.fi")
msg.add_attachment(open(OUTPUTFILE, "r", encoding="utf-8").read(), subtype='txt', filename='hello.txt')

s = smtplib.SMTP('smtp.pouta.csc.fi')
s.send_message(msg)
print("Email sent")

sys.exit()