#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A Square Class"""
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
