#!/usr/bin/python3

"""prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Takes two strings and returns a full name"""

    if type(first_name) is not str or type(last_name) is not str:
        raise TypeError("first_name must be a string or last_name must be a string")

    if len(first_name) == 0:
        return
    else:
        print("My name is {} {}".format(first_name, last_name), end="\n") 
