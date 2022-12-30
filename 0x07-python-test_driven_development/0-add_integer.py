#!/usr/bin/python3

"""A module that adds two integers and Returns
   their sum
"""


def add(a, b):
    """Accepts two integer and returns their sum"""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
