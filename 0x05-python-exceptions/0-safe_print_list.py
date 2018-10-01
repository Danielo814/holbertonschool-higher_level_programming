#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for idx in range(x):
            print("{}".format(my_list[idx]), end="")
    except IndexError:
        return idx
    else:
        return x
    finally:
        print("")
