#!/usr/bin/python3

def safe_print_integer(value):
    status = 0
    try:
        if (isinstance(value, int)):
            print("{:d}".format(value), end="\n")
            status = 1
        else:
            raise TypeError
    except TypeError:
        pass
    return status
