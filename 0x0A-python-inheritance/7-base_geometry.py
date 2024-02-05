#!/usr/bin/python3
""" Geometry class """


class BaseGeometry(object):
    """a Base geometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if a value parameter is int.
        Args:
           name (str): the name of the parameter.
           value (int): the parameter to validate.
        Raises:
           TypeError: if value is not int
           ValueError: if value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
