#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {}".format(number), end=" ")
if number < 0:
    number *= -1
    number = (number % 10) * -1
else:
    number %= 10
if number == 0:
    print("is {} and is 0".format(number))
if number < 6 and number != 0:
    print("is {} and is less than 6 and not 0".format(number))
if number > 5:
    print("is {} and is greater than 5".format(number))
