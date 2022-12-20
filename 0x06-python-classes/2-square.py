#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square class"""

    def __init__(self, size = 0):
        '''
            Initialize a Square Object.

        @self: 
            refers to the class instance.

        @size:
            The size of the square must be +ve integer.
        '''
        if type(size) not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
