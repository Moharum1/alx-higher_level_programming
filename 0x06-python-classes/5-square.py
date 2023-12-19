#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square.

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """
        Creates new instances of square (1 side).
        Args:
            size: size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Return the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size

        Args :
           value (int) : size of the square

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate th area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        print a square of a certin size
        """
        for colum in range(0, self.__size):
            for row in range(0, self.__size):
                print("{}".format("#"), end="")
            print("")
