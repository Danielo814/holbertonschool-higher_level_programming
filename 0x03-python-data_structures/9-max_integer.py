#!/usr/bin/python3
def max_integer(my_list=[]):
    retval = my_list[0]
    if my_list is None or len(my_list) < 1:
        return None
    for i in my_list:
        if i > retval:
            retval = i
    return retval
