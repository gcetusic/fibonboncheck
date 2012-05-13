#! /usr/bin/python

import urllib2
import sys
import pprint
import json

""" Get the Fibonacci series n-th member from a Django powered web application
    Only one argument is accepted for the script and simply passed on to the url.
    The argument HAS to be a pure Python int (no special html characters...)
    The normal result is a JSON string but the JSON could be malformed.
    In that case, the script just prints the received data.
"""
if not len(sys.argv)==2:
    help = sys.argv[0] + " fibnumber"
    print "Error: script needs exactly one argument\n" + help
    sys.exit(-1)

base_url = "http://localhost:8000/fibonacci/calc/" + sys.argv[1]
apirequest = urllib2.Request(base_url)

try:
    conn = urllib2.urlopen(apirequest)
    conn_status_http_code = conn.info().get('Status')
except:
    print "Url %s unresponsive" % (base_url)
    sys.exit(-1)

content = None
try:
    content_text = conn.read()
    content_json = json.load(conn)
    print("ResultMessage: %s" % (pprint.pformat(content_json)))
except ValueError:
    # For some reason, content doesn't seem to be parsable JSON
    print content_text
        