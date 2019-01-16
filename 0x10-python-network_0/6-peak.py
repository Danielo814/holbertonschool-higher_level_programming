#!/usr/bin/python3
"""
finds peak in list of unsorted ints
"""


def find_peak(list_of_integers):
    retval = 0
    if len(list_of_integers) == 0:
        return None
    for i in range(len(list_of_integers) - 1):
        next_index = i + 1
        if list_of_integers[next_index] >= list_of_integers[i]:
            retval = list_of_integers[i]
            if i != 0 and next_index != len(list_of_integers) - 1:
                retval = list_of_integers[next_index]
            else:
                continue
    return retval
