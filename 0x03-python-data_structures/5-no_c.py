#!/usr/bin/env python3
def no_c(my_string):
    str = ""
    for ch in my_string:
        if ch == 'c' or ch == 'C':
            continue
        str = str + ch
    return str
            
