#!/usr/bin/python3
"""
11-student module
"""


class Student:
    """
    class student
    """
    def __init__(self, first_name, last_name, age):
        """
        initialize Student attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retreives a dictionary representation of instance
        """
        return self.__dict__
