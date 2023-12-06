#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    desiredKey = []

    for key, valu in a_dictionary.items():
        if value == valu:
            desiredKey.append(key)

    for item in desiredKey:
        del a_dictionary[item]

    return a_dictionary
