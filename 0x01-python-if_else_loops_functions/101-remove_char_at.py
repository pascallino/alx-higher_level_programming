#!/usr/bin/env python3
def remove_char_at(str, n):
    remove_char_at = ''
    if n >= 0:
        for i in range(0, len(str)):
            if i == n:
                continue
            else:
                remove_char_at += str[i]
        return remove_char_at
    else :
        return str
