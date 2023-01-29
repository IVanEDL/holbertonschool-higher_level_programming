#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_dicc_sub = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
    result = 0
    prev = ""
    for numeral in roman_string:
        if prev + numeral in roman_dicc_sub:
            result = result - roman.get(prev) * 2
        result = result + roman.get(numeral)
        prev = numeral
    return result
