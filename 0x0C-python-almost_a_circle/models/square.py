"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
            A constructor for class objects

            Args:
                size (int) : The size of the square
                x (int, option) : The x position of the square
                y (int, option) : The y position of the square
                id (int, option) : The id of the class instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Setter for size propert"""
        return self.width
    
    @size.setter
    def size(self, val):
        """
            Getter for size propert

            args:
                val (int): the new value of size
        """
        self.width = val
        self.height = val

    def __str__(self):
        """
            Handle the String output of the class objects
        """
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}".format(self.width)

        return str_square + str_id + str_xy + str_wh
    
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
        myArgs = ["id", "size", "x", "y"]

        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if myArgs[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                setattr(self, myArgs[i], args[i])
        else:
            for key, val in kwargs.items():
                if key in myArgs:
                    if key == "size":
                        setattr(self, "width", val)
                        setattr(self, "height", val)
                    setattr(self, key, val)

    def to_dictionary(self):
        """Define the dictionary representation of a Square"""
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            if key == "size":
                dict_res[key] = getattr(self, "width")
            dict_res[key] = getattr(self, key)

        return dict_res