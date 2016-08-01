#!/usr/bin/env python

import urllib2
import lxml.html

url = 'http://www.flipkart.com/pigeon-favourite-ic-1800-w-induction-cooktop/p/itmdzzm5krfggpes?pid=ICTDZZM3SKDMH5CK&lid=LSTICTDZZM3SKDMH5CKG5CZSW&fm=merchandising&iid=M_9e6f9ded-fa3c-44a1-a7c6-6eeb0bb607a4.6c80fb22-600d-40f2-85eb-1447b07196f7&otracker=hp_omu_Deals%20of%20the%20Day_4_6c80fb22-600d-40f2-85eb-1447b07196f7_0'

try:
	html = urllib2.urlopen(url).read()
except urllib2.URLError as e:
	print "Error: ", e.reason
	html = None


tree = lxml.html.fromstring(html)
price_class = tree.find_class('selling-price omniture-field')[0]
price = price_class.text_content()
print price
