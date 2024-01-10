#!/usr/bin/python3
"""
a function that prints a dictionary by ordered keys.
"""


def print_sorted_dictionary(a_dictionary):
    for sk in sorted(a_dictionary):
        print(f"{sk}: {a_dictionary[sk]}", end="\n")
