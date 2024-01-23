#!/usr/bin/python3
"""
a module that defines a Square class
"""


class Square:
    """
    a class with a private instance attribute and
    checks for the size type and value
    """
    def __init__(self, size=0):
        if size and (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        if size and size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        returns area of a square
        """
        return self.__size ** 2
