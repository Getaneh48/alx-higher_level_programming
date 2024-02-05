#!/usr/bin/python3
"""a module that check if an object is a subclass of a given class"""


def inherits_from(obj, a_class):

    """returns True if it is inherited from a specified class
       otherwise False.
    """

    return issubclass(type(obj), a_class)
