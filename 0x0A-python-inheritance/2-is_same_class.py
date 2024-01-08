#!/usr/bin/python3
"""
    A module with is_same_class func
"""


def is_same_class(obj, a_class):
    """
        A function to check if obj is an instance of a_class

        Arg:
            obj : the object we want to check
            a_class : the class we use for checking

        Return:
            bool : is obj of same class as a_class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
