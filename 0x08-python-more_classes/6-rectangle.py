#!/usr/bin/python3
"""A rectangle Class"""


class Rectangle:
    # a Class type variable to detect number of instances
    number_of_instances = 0

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

        Rectangle.number_of_instances += 1

    def __str__(self):
        """
            Print the area of the rectangle using # char

            Return:
                str: rectangle shape
        """
        if self.width == 0 or self.height == 0:
            return ""

        rect = []

        for i in range(self.height):
            for j in range(self.width):
                rect.append("#")
            rect.append("\n")
        rect.pop()

        return "".join(rect)

    def __repr__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: the rectangle representation.
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
            A class destructor that print a string when an object's live ends
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """
            A function to computer the area of a rectangle

            Return:
                int: area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
            A function to computer the perimeter of a rectangle

            Return:
                int: perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)
