#!/usr/bin/python3
""" SUBCLASS RECTANGLE TO INHERIT FROM THE BASE"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class inherits base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(self.id)

    def __str__(self):
        """ instance representation of the object """
        str = f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}/{self.height}"
        return str

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        else:
            if width <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        else:
            if height <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """  x setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        else:
            if x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        else:
            if y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = y

    def area(self):
        """ Area of a Rectangle computed"""
        return self.__width * self.__height

    def display(self):
        """ display # rectangle """
        str = ""
        if self.width == 0 or self.height == 0:
            print(str)
            return
        for i in range(self.height):
            for j in range(self.width):
                str = str + '#'
            str = str + '\n'
        print("{}".format(str), end="")
