#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
nested_dict = {
        'b': 2,
        'c': {
            'd': 4,
            'e': 5,
            'f': {
                'h': 7,
                'g': 6
                }
            },
        'a': 1
        }
print_sorted_dictionary(nested_dict)
print_sorted_dictionary(a_dictionary)
