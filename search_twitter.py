#!/usr/bin/env python
from TwitterSearch import *
try:
	tso = TwitterSearchOrder()
	tso.set_keywords(['Joker'])
	tso.set_language('en')
	tso.set_include_entities(False)

	ts = TwitterSearch(
		consumer_key = 'R1gGSS3fs0BRpD4SwBReNlsVy',
		consumer_secret = 'z0CQem7vLPMFFYPshjRMFk8oL8NaCCzAETF5qHRvlOMj4jQJEr',
		access_token = '553284823-3UYFp7ZgBBjeWEP4IbGIGSdYA9pm8gAzE8NMebW4',
		access_token_secret = 'QOaEE07JGtGyhv2XD4AWVm9h3LsMxJw46VP7M5fJ5stM2'
	)	
	
	for tweet in ts.search_tweets_iterable(tso):
		print ('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ))
		print ('----------')

except TwitterSearchException as e:
	print (e)
