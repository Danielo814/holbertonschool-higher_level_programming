#!/usr/bin/python3
"""
4-inherits_from module that checks for subclass
"""


def inherits_from(obj, a_class):
    """
    checks if obj is sub class of a_class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
