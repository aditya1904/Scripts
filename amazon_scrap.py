#!/usr/bin/env python

import urllib2
import lxml.html
import sys

url = ''

try:
	html = urllib2.urlopen(url).read()
except urllib2.URLError as e:
	print 'Error: ', e.reason
	html = None
	sys.exit(1)

tree = lxml.html.fromstring(html)
price_class =  tree.cssselect('td.a-span12 > span#priceblock_saleprice')[0]
price = price_class.text_content()
print price

