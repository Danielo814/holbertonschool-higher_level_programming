#!/usr/bin/python3
"""
3-write_file module
"""


def write_file(filename="", text=""):
    """
    writes to a text file, returns num characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
