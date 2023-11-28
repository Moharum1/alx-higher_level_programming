#!/usr/bin/python3
import string


def uppercase(str):
    newStr = ""
    for char in str:
        if char in string.ascii_lowercase:
            newStr += chr(ord(char) - 32)
        else:
            newStr += char

    print("{}".format(newStr))
