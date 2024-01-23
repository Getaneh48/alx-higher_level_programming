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
        self.size = size

    def area(self):
        """
        returns area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size attribute to value
        @self:
            current instance

        @value:
            size value
        """
        if value and (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        if value and value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
