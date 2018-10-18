#!/usr/bin/python3
"""
rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set width
        """
        self.__width = value

    @property
    def height(self):
        """                                                                    
        getter for width                                                       
        """
        return self.__height

    @width.setter
    def height(self, value):
        """                                                                    
        set width                                                              
        """
        self.__height = value

    @property
    def x(self):
        """
        getter for x variable
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        self.__x = value

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for y
        """
        self.__y = value
