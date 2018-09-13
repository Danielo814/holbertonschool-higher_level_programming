#!/usr/bin/python3

import sys


if __name__ == "__main__":
    temp = 0
    for i in range(1, len(sys.argv)):
        temp += int(sys.argv[i])
    print(temp)
