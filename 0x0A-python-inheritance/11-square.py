#!/usr/bin/python3
"""Square class that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """a class represents a square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Returns the string representation of the class"""
        return ("[Square] {}/{}".format(self.__class__.__name__,
              self.__width / self.__height))
