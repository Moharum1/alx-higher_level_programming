#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = []
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        for item in my_list:
            newlist.append(item)
        newlist[idx] = element
        return newlist
