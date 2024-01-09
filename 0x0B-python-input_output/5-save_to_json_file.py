#!/usr/bin/python3
"""Define a function to save an obj file into a file"""
import json


def save_to_json_file(my_obj, filename):
    """Write the obj function in a certin file."""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
