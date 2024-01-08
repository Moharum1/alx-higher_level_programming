#!/usr/bin/python3
"""
    A module with is_kind_of_class func
"""


def inherits_from(obj, a_class):
    """
        A function to check if the object is an instance of a class 
            that inherited (directly or indirectly) from the specified class

        Arg:
            obj : the object we want to check
            a_class : the class we use for checking

        Return:
            bool
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)
