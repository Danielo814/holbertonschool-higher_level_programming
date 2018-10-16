#!/usr/bin/python3
"""
6-from_json_string module
"""

import json


def from_json_string(my_str):
    """
    returns an object represented by JSON string 'my_str'
    """
    return json.loads(my_str)
