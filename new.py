#!/usr/bin/env python

import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Added
from email.mime.image import MIMEImage
import urllib
import lxml.html

email = "adityamalu1@gmail.com"
password = getpass.getpass()

recipient = 'maluaditya12@gmail.com'
subject = 'Hi.'
Body = 'Todays xkcd.'
attachment = 'bob.png'

url = 'http://xkcd.com'
king = urllib.urlopen(url).read()
tree =  lxml.html.fromstring(king)
image_url = tree.cssselect('img')[1].get('src')
image_url = 'http:' + image_url
image = urllib.urlopen(image_url).read()
fd = open('bob.png','w')
fd.write(image)
fd.close()


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

print msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(email, password)

server.sendmail(email, recipient, msg.as_string())

