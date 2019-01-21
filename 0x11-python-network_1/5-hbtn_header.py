#!/usr/bin/python3
"""
sends request to URL, prints X-Request-Id value of header
"""
import requests
import sys


if __name__ == "__main__":
    value = requests.get(sys.argv[1])
    head = value.headers
    print(head.get('X-Request-Id'))
