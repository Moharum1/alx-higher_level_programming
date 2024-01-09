#!/usr/bin/python3
"""A module with one class Student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """
            A function define args needed by the obj of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrive the dic representation of class """
        res = {}
        if isinstance(attrs, list):
            for attr in attrs:
                if attr in self.__dict__:
                    res[attr] = self.__dict__[attr]
            return res
        return self.__dict__
