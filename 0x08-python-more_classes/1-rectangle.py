#!/usr/bin/python3
"""A rectangle Class"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, num):
        if type(num) is not int:
            raise TypeError("width must be an integer")
        elif num < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = num

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, num):
        if type(num) is not int:
            raise TypeError("height must be an integer")
        elif num < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = num
