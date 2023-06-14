#!/usr/bin/python3
def number_keys(a_dictionary):
    if a_dictionary:
        # len_1 = len(a_dictionary.keys())
        len_1 = 0
        for key, value in a_dictionary.items():
            len_1 += 1
        return len_1
