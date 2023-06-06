#!/usr/bin/env python3
def remove_char_at(str, n):
    remove_char_at = ''
    if n >= 0:
        str = str[:n] + str[n+1:]
        return str
    else :
        return str
