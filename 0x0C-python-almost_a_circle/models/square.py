#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square that inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor for square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        string representation of instance
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.height)

    @property
    def size(self):
        """
        getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for size attribute
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        assigns attributes
        """
        if args:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                if arg == 1:
                    self.size = args[arg]
                if arg == 2:
                    self.x = args[arg]
                if arg == 3:
                    self.y = args[arg]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        returns a dictionary representation of a Square
        """
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['size'] = self.size
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict
