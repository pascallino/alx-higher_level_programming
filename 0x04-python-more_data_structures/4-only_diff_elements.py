#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if not set_1 or not set_2:
        return
    else:
        set_new = set()
        # common_elements = set_1.intersection(set_2)
        # common_elements = set_1 && set_2
        common_elements = set_1 ^ set_2
        return common_elements
