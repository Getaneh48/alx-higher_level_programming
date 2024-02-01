#!/usr/bin/python3

"""prints a square with the character #"""


def print_square(size):
    """takes an integer value and prints a square
    with a character '#'.
    """

    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise ValueError("size must be an integer")

    i = 0
    j = 0
    while i < size:
        while j < size:
            print("#", end="")
            j += 1
        print("", end="\n")
        i += 1
        j = 0
