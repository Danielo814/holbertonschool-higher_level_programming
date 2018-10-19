#!/usr/bin/python3
"""
base module
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
