#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle

"""
    A module with the Square class
"""


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """
        init the object and take 1 input and validate the input

        Args:
            size : the size of the square
        """
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """A method to calculate the area of Square"""
        return self.__size * self.__size
