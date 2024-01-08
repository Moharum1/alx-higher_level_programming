#!/usr/bin/python3

class MyList(list):
    """
        A cusom list sub-class
    """

    def __init__(self):
        super().__init__()

    """
        A function that print the list in sorted order
    """
    def print_sorted(self):
        print(sorted(list(self)))
