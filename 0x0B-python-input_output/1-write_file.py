#!/usr/bin/python3
"""Define a text write file function"""


def write_file(filename="", text=""):
    """
        Change the contents of a UTF8 text file to stdout.

        Args:
            filename (str): a string describing the location of a file
            text (str): the new text you want to override in the file

        Return:
            int : number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
