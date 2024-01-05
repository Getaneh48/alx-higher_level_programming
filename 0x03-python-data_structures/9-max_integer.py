#!/usr/bin/python3
"""
a function that finds the biggest integer of a list.
"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = my_list[0]
    if len(my_list) == 1:
        return max
    for i in range(1, len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
    return max
