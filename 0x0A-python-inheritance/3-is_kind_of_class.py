#!/usr/bin/python3
"""
    A module with is_kind_of_class func
"""


def is_kind_of_class(obj, a_class):
    """
        A function to check if obj is an of a_class or obj of a sub_class of a_class

        Arg:
            obj : the object we want to check
            a_class : the class we use for checking

        Return:
            bool : is obj of same class as a_class
    """
    return isinstance(obj, a_class)
