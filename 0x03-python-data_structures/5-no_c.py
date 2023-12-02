#!/usr/bin/python3
def no_c(my_string):
    newStr = ""
    for char in my_string:
        if char == "C" or char == "c":
            pass
        else:
            newStr += char
    return newStr
