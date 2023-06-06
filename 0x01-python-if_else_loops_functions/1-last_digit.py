#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number > 5:
    print(f'Last digit of {number} is {last_digit} and is greater than 5')
elif number == 0:
    print("Last digit of {0:d} is {1:d} and is 0".format(number, last_digit))
else:
    if number < 0:
        last_digit = abs(number) % 10
    else:
        last_digit = number % 10
    print(f'Last digit of {number} is -{last_digit} and is less than 6 and not 0')
