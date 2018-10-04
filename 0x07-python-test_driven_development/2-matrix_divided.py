#!/usr/bin/python3
"""
2-matrix_divided module
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements in matrix by div
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by 0")
    if matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        length = len(matrix[0])
        if len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in i:
            if type(element) is not int and type(element) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
    return([list(map(lambda i: round(i / div, 2), j)) for j in matrix])
