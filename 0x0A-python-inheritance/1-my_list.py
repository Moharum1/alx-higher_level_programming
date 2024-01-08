#!/usr/bin/python3
"""
    A cusom list sub-class
"""
class MyList(list):
    """
        A cusom list sub-class
    """

    def __init__(self):
        """
        A function that init the super class
        """
        super().__init__()

    def print_sorted(self):
        """
        A function that print the list in sorted order
        """
        print(sorted(list(self)))
