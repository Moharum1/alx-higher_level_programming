#!/usr/bin/python3
"""Define a text write file function"""


def append_write(filename="", text=""):
    """
        append the contents of a UTF8 text file to stdout.

        Args:
            filename (str): a string describing the location of a file
            text (str): the new text you want to add to the file

        Return:
            int : number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
