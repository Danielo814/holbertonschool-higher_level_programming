#!/usr/bin/python3
def uppercase(str):
    retval = ""
    for i in range(0, len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            retval += chr(ord(str[i]) - 32)
        else:
            retval += chr(ord(str[i]))
        if i == len(str) - 1:
            retval += '\n'
    print("{}".format(retval), end="")
