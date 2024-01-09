#!/usr/bin/python3
"""Define a text read file function"""


def read_file(filename=""):
    """
        Print the contents of a UTF8 text file to stdout.

        Args:
            filename (str): a string describing the location of a file
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())
