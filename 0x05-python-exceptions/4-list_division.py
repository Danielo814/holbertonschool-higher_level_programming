#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    retval = 0
    for idx in range(list_length):
        try:
            retval = my_list_1[idx] / my_list_2[idx]
        except (ValueError, TypeError):
            print("wrong type")
            retval = 0
        except ZeroDivisionError:
            print("division by 0")
            retval = 0
        except IndexError:
            print("out of range")
            retval = 0
        finally:
            new_list.append(retval)
    return new_list
