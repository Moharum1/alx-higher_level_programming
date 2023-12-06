#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(list(a_dictionary.keys()))
    newDict = {i : a_dictionary[i] for i in keys}
    for key,value in newDict.items():
        print("{}: {}".format(key,value))

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)