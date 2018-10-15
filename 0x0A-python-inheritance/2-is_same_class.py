#!/usr/bin/python3
"""
2-is_same_class module that tests if an object is an
instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    returns True if obj is instance of a_class, False otherwise
    """
    if type(obj) != a_class:
        return False
    else:
        return True
