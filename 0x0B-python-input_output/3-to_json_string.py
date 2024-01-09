#!/usr/bin/python3
"""Define a string to json function"""
import json


def to_json_string(my_obj):
    """
        Convert string into json.

        Args:
            my_obj (str): the string you want to convert

        Return:
            json : the json form of string
    """
    return json.dumps(my_obj)
