#!/usr/bin/python3
"""
fetches 'https://intranet.hbtn.io/status' displays body of response
"""
import requests


if __name__ == '__main__':
    req = requests.get('https://intranet.hbtn.io/status')
    page = req.text
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(page), page))
