#!/usr/bin/python3
"""
a function that returns a new dictionary
with all values multiplied by 2
"""


def multiply_by_2(a_dictionary):
    return {key: val * 2 for key, val in a_dictionary.items()}
