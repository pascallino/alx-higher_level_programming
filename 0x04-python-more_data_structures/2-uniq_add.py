#!/usr/bin/env python3
def uniq_add(my_list=[]):
    if my_list:
        lst = set(my_list)
        return sum(lst)