#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if len(a_dictionary.keys()) > 0:
        if key in a_dictionary:
            a_dictionary[key] = value
            return a_dictionary
        else:
            new_entry = {key: value}
            a_dictionary.update(new_entry)
            return a_dictionary
