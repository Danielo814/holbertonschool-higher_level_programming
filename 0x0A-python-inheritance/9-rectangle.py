#!/usr/bin/python3
"""
9-rectangle module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        initialize width and height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        str method to print rectangle descriptions
        """
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
