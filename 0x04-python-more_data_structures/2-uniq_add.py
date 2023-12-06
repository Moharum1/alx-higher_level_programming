#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    sum = 0
    for ele in uniq_list:
        sum += ele
    return sum
