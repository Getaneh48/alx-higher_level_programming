#!/usr/bin/python3
"""
a function def roman_to_int(roman_string):
that converts a Roman numeral to an integer.
"""


def roman_to_int(roman_string):
    if type(roman_string).__name__ != 'str' or \
            roman_string is None:
        return 0
