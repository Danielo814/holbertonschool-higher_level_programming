#!/usr/bin/python3
"""
4-append_write module
"""


def append_write(filename="", text=""):
    """
    appends 'text' to end of file 'filename' and returns number of
    characters appended
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
