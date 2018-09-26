#!/usr/bin/python3
def weight_average(my_list=[]):
    retval = 0
    temp = 0
    if my_list == []:
        return 0
    for i in range(0, len(my_list)):
        for j in range(0, 1):
            retval += my_list[i][j] * my_list[i][j + 1]
            temp += my_list[i][j + 1]
    retval /= temp
    return retval
