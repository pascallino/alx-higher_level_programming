#!/usr/bin/python3
""" append_after """


def append_after(filename="", search_string="", new_string=""):
    """ Function to append text after the search string in a file """
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if search_string in lines[i]:
            lines.insert(i + 1, new_string)

    with open(filename, 'w') as file:
        file.writelines(lines)
