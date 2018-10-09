#!/usr/bin/python3
"""
9-rectangle module
"""


class Rectangle:
    """
    rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializes a rectangle class with values
        height and width
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """
        returns the area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        string representation of a rectangle
        """
        symbol = str(self.print_symbol)
        retval = ""
        for h in range(self.__height):
            for w in range(self.__width):
                retval += symbol
            if h != self.__height - 1:
                retval += '\n'
        return retval

    def __repr__(self):
        """
        returns a string representation of the rectangle to be able
        to recreate a new instance using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        method gets called whenever an instance is about to be destroyed
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle instance with width==height==size
        """
        return cls(size, size)
