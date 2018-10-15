#!/usr/bin/python3
"""
0-lookup module
"""


def lookup(obj):
    """
    returns list of abailable attributes and methods available to obj
    """
    return dir(obj)
