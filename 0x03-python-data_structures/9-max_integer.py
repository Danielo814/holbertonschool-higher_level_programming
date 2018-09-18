#!/usr/bin/python3
def max_integer(my_list=[]):
    retval = my_list[0]
    if my_list is None or my_list is []:
        return None
    else:
        for i in my_list:
            if i > retval:
                retval = i
        return retval
