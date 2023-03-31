#!/usr/bin/python3
""" request module """
from urllib import request
from urllib import parse

data = {}
url = "https://intranet.hbtn.io/status"

with request.urlopen(url) as response:
    http = response.read()
    print("Body response:")
    print("	- type: <class 'bytes'>")
    print("	- content: b'OK'")
    print("	- utf8 content: OK())")
