#!/usr/bin/python3
""" BASE MODEL CLASS / SUPER CLASS"""


class Base:
    """ base class from which other classes will be derived"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor __init__ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects