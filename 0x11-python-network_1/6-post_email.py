#!/usr/bin/python3
"""
takes in a URL as email address and sends POST request
"""
import sys
import requests


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1])
    print(req.text)
