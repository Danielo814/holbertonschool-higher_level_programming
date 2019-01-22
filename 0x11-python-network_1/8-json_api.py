#!/usr/bin/python3
"""
sends a post request with letter as arg
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 2:
        q = ""
    else:
        q = sys.argv[1]
    try:
        req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        new_dict = req.json()
        name = new_dict.get('name')
        id = new_dict.get('id')
        if len(new_dict) != 0:
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
