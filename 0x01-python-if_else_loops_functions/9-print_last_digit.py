#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0 :
        print_last_digit = abs(number) % 10
    else :
        print_last_digit = number % 10
    print("{}".format(print_last_digit), end="")
    return print_last_digit
