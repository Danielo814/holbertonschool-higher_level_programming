#!/usr/bin/python3
"""
5-to_json_string module
"""


import json


def to_json_string(my_obj):
    """
    converts my_obj to JSON representation of an object
    """
    return json.dumps(my_obj)
