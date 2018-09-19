#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) is not 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    elif sys.argv[2] is not "+" and sys.argv[2] is not "-"\
         and sys.argv[2] is not "*" and sys.argv[2] is not "/":
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    elif sys.argv[2] == '+':
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3],
                                    add(int(sys.argv[1]), int(sys.argv[3]))))

    elif sys.argv[2] == '-':
        print("{} - {} = {}".format(sys.argv[1], sys.argv[3],
                                    sub(int(sys.argv[1]), int(sys.argv[3]))))

    elif sys.argv[2] == '*':
        print("{} * {} = {}".format(sys.argv[1], sys.argv[3],
                                    mul(int(sys.argv[1]), int(sys.argv[3]))))

    elif sys.argv[2] == '/':
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3],
                                    div(int(sys.argv[1]), int(sys.argv[3]))))
