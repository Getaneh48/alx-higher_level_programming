#!/usr/bin/python3
"""
a function that returns a key with the
biggest integer value.
"""


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary):
        return None
    return max(a_dictionary)
