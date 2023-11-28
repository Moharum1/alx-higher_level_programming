#!/usr/bin/python3

def uppercase(str):
    newStr = ""
    for char in str:
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            newStr += chr(ord(char) - 32)
        else:
            newStr += char

    print("{}".format(newStr))
