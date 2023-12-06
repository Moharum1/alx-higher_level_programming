#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = {i : a_dictionary[i] * 2 for i in a_dictionary}
    return newDict
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print(a_dictionary)
print("--")
print(new_dict)