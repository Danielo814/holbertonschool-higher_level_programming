#!/usr/bin/python3
"""
2-read_lines module
"""


def read_lines(filename="", nb_lines=0):
    """
    read nb_lines number of lines from filename and prints to stdout
    """
    i = 0
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for line in f:
                if i < nb_lines:
                    print(line, end="")
                i += 1
