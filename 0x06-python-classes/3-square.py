#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square class"""

    def __init__(self, size=0):
        '''
            Initialize a Square Object.

        @self:
            refers to the class instance.

        @size:
            The size of the square must be +ve integer.
        '''
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        '''
            Returns the area of the square.

        @self:
            Refers to the class instance.
        '''
        return self.__size * self.__size
