#!/usr/bin/python3
"""
a function that adds all unique integers in a
list (only once for each integer).
"""


def uniq_add(my_list=[]):
    sum = 0
    uniq_list = list(set(my_list))
    for n in uniq_list:
        sum += n
    return sum
