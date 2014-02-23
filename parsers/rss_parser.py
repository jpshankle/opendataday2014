# -*- coding: utf-8 -*-
import feedparser
from HTMLParser import HTMLParser

python_wiki_rss_url = "http://portal.goszakup.gov.kz/portal/index.php/ru/rss"

feed = feedparser.parse( python_wiki_rss_url )
description = feed['entries'][0]['description']
search_string = "Адрес доставки:"
entry = dict()
amount_field = dict()
amount_field['source'] = "Общая сумма:"
amount_field['dest'] = "amount"
award_date = "Дата начала приема заявок:"
agency_field = "Организация:"
pair_completed = False
key_name = ''
inside_b_tag = None
key_found = None

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
    	global inside_b_tag
        print "Encountered a start tag:", tag
        if tag == "b":
        	inside_b_tag = True
        	print inside_b_tag
    def handle_endtag(self, tag):
    	global inside_b_tag
        print "Encountered an end tag :", tag
        if tag == "b":
        	inside_b_tag = False
    def handle_data(self, data):
        global key_found
        print "Encountered some data  :", data
        # find the key first
        if data.find(unicode(amount_field['source'], encoding="utf-8")) >= 0:
        	# if we're inside a b-tag, it's a key
        	if inside_b_tag:
        		key_name = amount_field['dest']
        		key_found = True
        		print "key found"
		# after the key is found, the next field will be the data
		if inside_b_tag == False and key_found == True:
			print "value found"
			entry[key_name] = data

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(description)
print entry