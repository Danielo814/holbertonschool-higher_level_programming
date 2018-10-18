#!/usr/bin/python3
"""
base module
"""


class Base:
    """
    base class to manage id attribute in all future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method for setting id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
