#!/usr/bin/python3
""" text indent """


def text_indentation(text):
    """ indentation function """
    newtext = ""
    flag = 0;
    last = 0;
    count = 0;
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if count == 0 and char == ' ':
            continue
        if flag == 1 and char == ' ':
            continue
        else:
            count = 1
            flag = 0
            newtext += char
            if char in ['.', '?', ':']:
                newtext += "\n\n"
                flag = 1
    print("{}".format(newtext[-len(newtext):last]), end="")
