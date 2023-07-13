#!/usr/bin/python3
""" SQUARE CLASS INHERITS FROM RECTANGLE CLASS"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class will derived from the Rectangle Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor __init__ """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str representation of the obkject """
        str = f"[Square] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}"
        return str

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value
