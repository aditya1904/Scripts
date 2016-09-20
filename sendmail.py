#!/usr/bin/env python

import smtplib
import getpass

email = "anonbridge1@gmail.com"
password = getpass.getpass()

recipient = raw_input('To: ')
subject = raw_input('Subject: ')
Body = raw_input('Body: ')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(email, password)

BODY = '\r\n'.join(['Subject: %s' % subject, '', Body])

server.sendmail(email, recipient, BODY)
print ('email sent')
