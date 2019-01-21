#!/usr/bin/python3
"""
fetches 'https://intranet.hbtn.io/status' and displays body of response
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
    print('Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'
          .format(type(body), body, body.decode('utf-8')))
