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
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        '''
            sets a size attribute to a given value.

        @self:
            refers to the class instance.

        @value:
            integer value to be set to the size attrib.
        '''
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        '''
            Returns the area of the square.

        @self:
            Refers to the class instance.
        '''
        return self.__size * self.__size
