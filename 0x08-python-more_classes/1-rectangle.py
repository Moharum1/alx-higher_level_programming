#!/usr/bin/python3
"""A rectangle Class"""


class Rectangle:
    """
        Class that define the basic properties of a Rectangle

        Args :
            width (int) : width of the square
            height (int) : height of the square
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            A getter for the width property

            Return:
                int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, num):
        """
            A setter for the width property Which

            Args:
                num (int): width of the rectangle            
            Raise:
                TypeError: if the input isn't number
                ValueError: if the input is less than 0
        """
        if not isinstance(num, int):
            raise TypeError("width must be an integer")
        elif num < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = num

    @property
    def height(self):
        """
            A getter for the height property

            Return:
                int: width of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, num):
        """
            A setter for the Height property Which

            Args:
                num (int): height of the rectangle            
            Raise:
                TypeError: if the input isn't number
                ValueError: if the input is less than 0
        """
        if not isinstance(num, int):
            raise TypeError("height must be an integer")
        elif num < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = num
