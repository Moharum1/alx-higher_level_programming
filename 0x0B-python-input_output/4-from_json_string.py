#!/usr/bin/python3
"""Define a json to py object function"""
import json


def from_json_string(my_str):
    """
        Convert object into json.

        Args:
            my_str (str): the string you want to convert

        Return:
            obj : the python object representation of string
    """
    return json.load(my_str)
