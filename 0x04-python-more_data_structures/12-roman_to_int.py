#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_Numbers = {"I": 1, "V": 5, "X": 10,
                     "L": 50, "C": 100, "D": 500, "M": 100}
    sub_notation = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    prev_key = roman_string[0]
    sum = 0

    if len(roman_string) == 2:
        if str(prev_key + roman_string[1]) not in sub_notation:
            currentNum = roman_Numbers.get(prev_key)
            sum += currentNum + roman_Numbers.get(roman_string[1])
        else:
            sum += sub_notation.get(prev_key + roman_string[1])
        return sum

    for char in roman_string:
        if str(prev_key + char) not in sub_notation:
            currentNum = roman_Numbers.get(char)
            sum += currentNum
        else:
            sum += sub_notation.get(prev_key + char)

        prev_key = char
    return sum
