#!/usr/bin/python3
""" Geometry class """


class BaseGeometry(object):
    """a Base geometry class"""

    def area(self):
        raise Exception("area() is not implemented")
