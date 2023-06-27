#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A Square Class"""

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    def __init__(self, size=0):
        self.__size = size
