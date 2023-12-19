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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
