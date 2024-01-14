#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            A constructor for class objects

            Args:
                width (int) : The width of the rectangle
                height (int) : The hight of the rectangle
                x (int, option) : The x position of the rectangle
                y (int, option) : The y position of the rectangle
                id (int, option) : The id of the class instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        Base.__init__(self, id)

    @property
    def width(self):
        """A getter for the width private property"""
        return self.__width

    @width.setter
    def width(self, val):
        """
            A setter for the width property

            args:
                val (int): the new value of width

            Raise:
                TypeError : if val is not Int
                ValueError : if val is less than 0
        """
        if isinstance(val, int):
            if val > 0:
                self.__width = val
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """A getter for the height private property"""
        return self.__height

    @height.setter
    def height(self, val):
        """
            A setter for the Height property

            args:
                val (int): the new value of Height

            Raise:
                TypeError : if val is not Int
                ValueError : if val is less than 0
        """
        if isinstance(val, int):
            if val > 0:
                self.__height = val
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """A getter for the x private property"""
        return self.__x

    @x.setter
    def x(self, val):
        """
            A setter for the x property

            args:
                val (int): the new value of x

            Raise:
                TypeError : if val is not Int
        """
        if isinstance(val, int):
            if val >= 0:
                self.__x = val
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """A getter for the y private property"""
        return self.__y

    @y.setter
    def y(self, val):
        """
            A setter for the y property

            args:
                val (int): the new value of y

            Raise:
                TypeError : if val is not Int
        """
        if isinstance(val, int):
            if val >= 0:
                self.__y = val
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """
            A method to compute the area of the rectangle

            Return :
                int : Rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """
            A method to print the shape of the rectangle
        """
        for _ in range(self.__y):
            print("")

        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
            Handle the String output of the class objects
        """
        str_rectangle = "[Rectangle] "
        
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """
            Update the Rectangle class according to the number of args

            args:
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
        """
        myArgs = ["id", "width", "height", "x", "y"]

        for i in range(len(args)):
            setattr(self, myArgs[i], args[i])

        for key, val in kwargs.items():
            if key in myArgs:
                setattr(self, key, val)

    def to_dictionary(self):
        """Define the dictionary representation of a Rectangle"""
        list_atr = ["x", "y", "id", "height", "width"]
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res