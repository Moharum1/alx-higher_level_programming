#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum = 0
    dom = 0

    for item in my_list:
        sum += item[0] * item[1]
        dom += item[1]

    return sum/dom
