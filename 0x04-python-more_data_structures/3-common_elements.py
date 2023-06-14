#!/usr/bin/env python3
def common_elements(set_1, set_2):
    if not set_1 and not set_2:
        return
    else:
        set_new = set()
        # common_elements = set_1.intersection(set_2)
        # common_elements = set_1 && set_2
        for item in set_1:
            if item in set_2:
                set_new.add(item)
        return set_new
