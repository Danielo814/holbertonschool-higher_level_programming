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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string representation of list_objs to a file
        """
        file_name = "{}.json".format(cls.__name__)
        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(cls.to_dictionary(obj))
        with open(file_name, mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(new_list))
