#!/usr/bin/python3
"""
1-rectangle module
"""


class Rectangle:
    """
    rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        initializes a rectangle class with values
        height and width
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter for width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets a width according to parameter 'value'
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        getter for height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets a height according to parameter 'value'
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
