#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number > 5 :
    print(f"Last digit of {number:d} is {last_digit:d} and is greater than 5")
elif number == 0 :
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
elif number < 6 and number != 0 :
    if number < 0 :
        pos = number * -1
        last_digit = pos % 10
    print(f"Last digit of {number:d} is {last_digit:d} and is less than 6 and not 0")
