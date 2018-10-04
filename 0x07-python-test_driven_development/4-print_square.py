#!/usr/bin/python3
"""
4-print_square module
"""


def print_square(size):
    """
    prints a square that bases its size on the value of 'size'
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
