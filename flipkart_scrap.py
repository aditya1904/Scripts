#!/usr/bin/env python

''' The script was written so that you can check the price of a product daily without even going to the flipkart website. You need to put the product url and then whenever you want to check the price, you can just run the script. Buy the product whenever you feel the price is less.
'''
import urllib2
import lxml.html
import sys

url = 'http://www.flipkart.com/pigeon-favourite-ic-1800-w-induction-cooktop/p/itmdzzm5krfggpes?pid=ICTDZZM3SKDMH5CK&lid=LSTICTDZZM3SKDMH5CKG5CZSW&fm=merchandising&iid=M_9e6f9ded-fa3c-44a1-a7c6-6eeb0bb607a4.6c80fb22-600d-40f2-85eb-1447b07196f7&otracker=hp_omu_Deals%20of%20the%20Day_4_6c80fb22-600d-40f2-85eb-1447b07196f7_0' #This needs to be changed for every product you want to buy.

try:
	html = urllib2.urlopen(url).read()
except urllib2.URLError as e:
	print "Error: ", e.reason
	html = None
	sys.exit(1)


tree = lxml.html.fromstring(html)
price_class = tree.find_class('selling-price omniture-field')[0]  #Apparently this is the class in which flipkart price is written. Found Out in th the html of page using firebug lite.
price = price_class.text_content()
print price
