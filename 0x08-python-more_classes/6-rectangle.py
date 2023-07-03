#!/usr/bin/python3
""" A Rectangle Module """


class Rectangle:
    number_of_instances = 0
    """ public intance variable number_of_instances (int) """
    """ A class that should define a redctangle """
    def __init__(self, width=0, height=0):
        """ __init__ """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ __str__ """
        str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str += "#"
            if i != self.__height - 1:
                str += "\n"
        return str

    def __repr__(self):
        """ repr """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints a string when an instance has been deleted"""
        print("Bye rectangle...")
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """ Area """
        return self.__height * self.__width

    def perimeter(self):
        """ permiter """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
