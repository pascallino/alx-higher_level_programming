#!/usr/bin/python3
def islower(c):
    if c == "":
        return False
    elif len(c) == 0:
        return False
    elif (c >= 'a' and c <= 'z'):
        return True
    else:
        return False
