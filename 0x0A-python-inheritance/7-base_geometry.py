#!/usr/bin/python3
"""
    A module with BaseGeometry class
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