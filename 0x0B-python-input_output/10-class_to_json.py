#!/usr/bin/python3
"""
10-class_to_json module
"""


def class_to_json(obj):
    """
    returns dictionary description with simple data structure
    """
    return obj.__dict__
