#!/usr/bin/python3

def safe_print_integer(value):
    status = 0
    try:
        value = int(value)
        print("{:d}".format(value), end="\n")
        status = 1
    except ValueError:
        status = 0
        pass
    return status
