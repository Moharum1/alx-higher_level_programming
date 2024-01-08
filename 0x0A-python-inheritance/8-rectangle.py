#!/usr/bin/python3
"""
    A module with Rectangle class and BaseGeometry Class
"""


class BaseGeometry():
    """A BaseGeometry Class"""

    def area(self):
        """A function to print the area of the Geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            A function to check if value is a valid int that
                is greater than zero

            Raise:
                TypeError : if value not integer
                ValueError : if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A Rectangle Class that inherit BaseGeometry"""

    def __init__(self, width, height):
        """
        init the object and take 2 input and validate the input

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.__width = width
        self.__height = height

        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """A function to print the area of the Geometry"""
        raise Exception("area() is not implemented")
