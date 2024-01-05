#!/usr/bin/python3
"""
a function that removes all characters c and C from a string.
"""


def no_c(my_string):
    nstring = ""
    for c in my_string:
        if c == 'c' or c == 'C':
            continue
        nstring += c
    return nstring
