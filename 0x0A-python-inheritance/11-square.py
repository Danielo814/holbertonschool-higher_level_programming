#!/usr/bin/python3
"""
11-square module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        initializes size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        computes area
        """
        return self.__size * self.__size

    def __str__(self):
        """
        string representation of object
        """
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__size, self.__size)
