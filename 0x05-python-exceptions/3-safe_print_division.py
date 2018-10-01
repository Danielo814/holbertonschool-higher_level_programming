#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        retval = a / b
    except ZeroDivisionError:
        retval = None
    finally:
        print("Inside result: {}".format(retval))
        return retval
