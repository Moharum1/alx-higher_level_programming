#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newLis = []
    for item in my_list:
        if item % 2 == 0:
            newLis.append(True)
        else:
            newLis.append(False)
    return newLis
