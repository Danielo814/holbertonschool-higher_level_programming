#!/usr/bin/python3
"""
Square class
"""


class Square:
    """
    square private instance attritute size
    """
    def __init__(self, size=0):
        """
        instantiation with size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
