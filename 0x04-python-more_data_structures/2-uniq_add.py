#!/usr/bin/python3
def uniq_add(my_list=[]):
    retval = 0
    uniq = set(my_list)
    for i in uniq:
        retval += i
    return retval
