#!/usr/bin/python3
def best_score(a_dictionary):
    temp = 0
    empty = ""
    if a_dictionary is None or if a_dictionary == {}:
        return None
    for k, v in a_dictionary.items():
        if a_dictionary[k] > temp:
            temp = a_dictionary[k]
            empty = k
    return empty
