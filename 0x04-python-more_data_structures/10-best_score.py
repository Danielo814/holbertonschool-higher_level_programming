#!/usr/bin/python3
def best_score(a_dictionary):
    temp = 0
    empty = ""
    if a_dictionary is None or a_dictionary == {}:
        return None
    for k in a_dictionary.keys():
        if a_dictionary[k] > temp:
            temp = a_dictionary[k]
            empty = k
    return empty
