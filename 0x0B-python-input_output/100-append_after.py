#!/usr/bin/python3
""" append_after """


def append_after(filename="", search_string="", new_string=""):
    """ function to append text after the serach string """
    with open(filename, 'r') as file:
        lines = file.readlines()

        str = ""
        count = -1
        for line in lines:i
            words = line.split()
            for word in words:
                if word == search_string:
                    count += 1
                    lines.insert(count, new_string)
                    break
    with open(filename, 'w') as file:
        file.write(''.join(lines))
