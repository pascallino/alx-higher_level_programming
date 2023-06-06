#!/usr/bin/python3
i = 97
while i <= 122:
    if i == 113 or i == 101:
        i += 1
        continue
    print("{}".format(chr(i)), end="")
    i += 1
