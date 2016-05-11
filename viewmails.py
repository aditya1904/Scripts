#!/usr/bin/env python
import imapclient
import pyzmail
import datetime
mymail = imapclient.IMAPClient('imap.gmail.com', ssl=True)
mymail.login('anonbridge1@gmail.com','anonbridge3')
mymail.select_folder('INBOX', readonly=False)
uids = mymail.search(['ALL'])
rawmessage = mymail.fetch(uids, ['BODY[]'])
for i in uids:
	message = pyzmail.PyzMessage.factory(rawmessage[i]['BODY[]'])
	print 'from: ', message.get_addresses('from')
	print 'to: ', message.get_addresses('to')
	print 'cc: ', message.get_addresses('cc')
	print 'bcc: ', message.get_addresses('bcc')
	print 'SUBJECT: ', message.get_subject()
	if message.text_part:
		print message.text_part.get_payload().decode(message.text_part.charset)
	if message.html_part:
		print message.html_part.get_payload().decode(message.html_part.charset)
	print '+-' * 40
mymail.logout()
	

