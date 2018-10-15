#!/usr/bin/python3
"""
3-is_kind_of_class module that checks if object is instance of
or if the object is an instance of a class that inherited from a
specified class
"""


def is_kind_of_class(obj, a_class):
    """
    True if isinstance, False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
