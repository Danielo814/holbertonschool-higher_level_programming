#!/usr/bin/python3
def roman_to_int(roman_string):
    retval = 0
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or type(roman_string) != str:
        return 0
    for i in roman_string:
        if i in my_dict:
            retval += my_dict[i]
    for compare in range(0, len(roman_string) - 1):
        if my_dict[roman_string[compare]] < my_dict[roman_string[compare + 1]]:
            retval -= 2
    return retval
