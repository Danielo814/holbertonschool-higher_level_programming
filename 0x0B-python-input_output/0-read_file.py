#!/usr/bin/python3
"""
0-read_file module that reads a file and prints to stdout
"""


def read_file(filename=""):
    """
    opens file 'filename' and prints contents to stdout
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
