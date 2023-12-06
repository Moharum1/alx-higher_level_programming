#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res = (set_1 - set_2).union(set_2 - set_1)
    return res


