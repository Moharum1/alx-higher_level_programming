#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
    A module with Rectangle class and BaseGeometry Class
"""


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

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))