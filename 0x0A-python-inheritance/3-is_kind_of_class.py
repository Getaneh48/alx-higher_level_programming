#!/usr/bin/python3
"""a module that check if an object is an
   instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):

    """returns True if it is inherited from a specified class
       otherwise False.
    """

    return isinstance(obj, a_class)
