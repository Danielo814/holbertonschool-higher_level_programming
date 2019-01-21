#!/usr/bin/python3
"""
sends request to url and prints error code
"""
from urllib import error, request
import sys


if __name__ == "__main__":
    try:
        req = request.Request(sys.argv[1])
        with request.urlopen(req) as f:
            page = f.read()
        print(page.decode('utf-8'))
    except:
        except error.HTTPError as err:
            print("Error code: {}".format(err.code))
