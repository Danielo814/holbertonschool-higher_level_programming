#!/usr/bin/python3
"""
1-number_of_lines module
"""


def number_of_lines(filename=""):
    """
    returns the number of lines of a text file
    """
    numlines = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            numlines += 1
    return numlines
