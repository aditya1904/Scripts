#!/usr/bin/env python
##This one needs a lot of improvment 
## A cleaner version update soon.
import urllib2
import lxml.html
import sys

url = 'http://www.amazon.in/Sony-MDR-ZX110A-Stereo-Headphone-White/dp/B00KGZZ824/ref=sr_1_1?ie=UTF8&qid=1470725118&sr=8-1&keywords=sony+mdr+zx110a'

try:
	html = urllib2.urlopen(url).read()
except urllib2.URLError as e:
	print 'Error: ', e.reason
	html = None
	sys.exit(1)

tree = lxml.html.fromstring(html)
price_class =  tree.cssselect('td.a-span12 > span#priceblock_saleprice')[0]
name_class = tree.cssselect('h1#title > span#productTitle')[0]
name = name_class.text_content()
try:
    price_class_deal =  tree.cssselect('td.a-span12 > span#priceblock_dealprice')[0]
    deal = price_class.text_content()
    print "dealprice" + deal
except:
    pass

price = price_class.text_content()
name = name.replace('\n','')

print name
print "Saleprice" + price

