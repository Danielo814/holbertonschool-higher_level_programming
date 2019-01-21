#!/usr/bin/python3
"""
takes in a URL and sends a post request, also displays body of response
"""
import sys
from urllib import request
from urllib import parse


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    data = parse.urlencode(email)
    data = data.encode('utf-8')
    quest = request.Request(sys.argv[1], data)
    with request.urlopen(quest) as response:
        page = response.read()
    print(page.decode('utf-8'))
