#!/usr/bin/python3
"""
    A module with class MyList
"""


class MyList(list):
    """
        A cusom list sub-class
    """

    def print_sorted(self):
        """
        A function that print the list in sorted order
        """
        print(sorted(list(self)))
