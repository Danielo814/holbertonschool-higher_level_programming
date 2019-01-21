#!/usr/bin/python3
"""
sends request to URL, prints X-Request-Id value of header
"""
from urllib import request
import sys


if __name__ == "__main__":
    value = request.Request(sys.argv[1])
    with request.urlopen(value) as response:
        page = response.headers.get('X-Request-Id')
    print(page)
