#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square.

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0, pos=(0, 0)):
        """
        Creates new instances of square (1 side).
        Args:
            size: size of the square.
        """
        self.__size = size
        self.__position = pos

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

    @property
    def position(self):
        """Return the position of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the size

        Args :
           value (int) : a pair of type (int * int)

        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate th area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        print a square of a certin size
        """
        if self.__size == 0:
            print()

        for row in range(0, self.__size):
            for i in range(0, self.position[1]):
                print()
            for pos in range(0, self.position[0]):
                print(" ", end="")
            print("#" * (self.__size))
