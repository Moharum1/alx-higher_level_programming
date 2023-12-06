#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(list(a_dictionary.keys()))
    newDict = {i: a_dictionary[i] for i in keys}
    for key, value in newDict.items():
        print("{}: {}".format(key, value))
