#!/usr/bin/python3
"""Define a class to json function"""
import json


def class_to_json(obj):
    """
        Convert class into json.

        Args:
            obj (str): the class you want to convert

        Return:
            json : the json form of string
    """
    structure = {}
    if hasattr(obj, "__dict__"):
        structure = obj.__dict__.copy()
    return structure
