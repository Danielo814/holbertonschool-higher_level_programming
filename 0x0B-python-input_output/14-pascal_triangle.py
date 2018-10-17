#!/usr/bin/python3
"""
14-pascal_triangle module
"""


def pascal_triangle(n):
    """
    returns a list of integers representing pascal's triangle of n
    """
    newlist = []
    for row in range(n):
        newlist.append([])
        for column in range(row + 1):
            if column == 0 or column == row:
                newlist[row].append(1)
            else:
                newlist[row].append(newlist[row - 1][column - 1] +
                                    newlist[row - 1][column])
    return newlist
