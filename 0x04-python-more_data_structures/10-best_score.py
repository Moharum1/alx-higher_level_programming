#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    bestScore = 0
    name = ""
    for key, value in a_dictionary.items():
        if value > bestScore:
            bestScore = value
            name = key
    return name
