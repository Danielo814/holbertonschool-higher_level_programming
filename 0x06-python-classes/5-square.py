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
        self.size = size

    @property
    def size(self):
        """
        size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        method that prints the square with the character '#'
        """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print("")
