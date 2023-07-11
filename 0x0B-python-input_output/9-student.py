#!/usr/bin/python3
""" Student module """


def class_to_json(obj):
    """ function to return dict attributes """
    return obj.__dict__


class Student:
    """  Class to define a student"""
    def __init__(self, first_name, last_name, age):
        """  __init__ function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return dict of itself  self.__dict__"""
        return class_to_json(self)
