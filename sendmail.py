#!/usr/bin/env python

import smtplib
import getpass

email = "anonbridge1@gmail.com"
password = getpass.getpass()

recipient = raw_input('To: ')
subject = raw_input('Subject: ')
Body = raw_input('Body: ')

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Added
from email.mime.image import MIMEImage

attachment = 'bob.jpg'

msg = MIMEMultipart()
msg["To"] = recipient
msg["From"] = email
msg["Subject"] = subject

msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % (Body, attachment), 'html')  
msg.attach(msgText)   # Added, and edited the previous line

fp = open(attachment, 'rb')                                                    
img = MIMEImage(fp.read())
fp.close()
img.add_header('Content-ID', '<{}>'.format(attachment))
msg.attach(img)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(email, password)

BODY = '\r\n'.join(['Subject: %s' % subject, '', Body])

server.sendmail(email, recipient, msg.as_string())
print ('email sent')
