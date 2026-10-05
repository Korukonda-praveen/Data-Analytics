'''
Email Automation using python --> first we need to turn on 2-step verifiction 
create app password
smtplib--> simple mail transfer protocol
from email.mime.multipart import MIMEMultipart --> used to create email
from email.mime.text import MIMEText--> used to create text
MIME-->Multipurpose internet mail extension
'''
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase # to add up our attachment
from email import encoders
import random
import os

# first we need to connect to gmail server
server = smtplib.SMTP('smtp.gmail.com', 587)

# starting the connection
server.starttls()

# login to email
server.login('your email_id', 'app password')

# otp and mail format and sending attachement
otp = random.randint(1000, 9999)
msg = MIMEMultipart()
From = 'praveen545792@gmail.com'
To = 'praveen545792@gmail.com'
Subject = 'Email Automation project using python'

# Get exact path to the file in the same directory as this script
attach = os.path.join(os.path.dirname(__file__), 'tony.jpeg')

msg['From'] = From
msg['To'] = To
msg['Subject'] = Subject
body = f'attachement test for mail automation using python\nOTP: {otp}'
msg.attach(MIMEText(body))

part = MIMEBase('application', 'octet-stream')
part.set_payload(open(attach, 'rb').read())

# finally we will convert above as string
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
msg.attach(part)

text = msg.as_string()
server.sendmail(From, To, text)

server.quit()
print('mail sent boss')

input_ = int(input('enter your otp:'))
if input_ == otp:
    print('correct otp')
else:
    print('incorrect otp')
