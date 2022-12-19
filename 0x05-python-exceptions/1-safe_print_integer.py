#!/usr/bin/python3

def safe_print_integer(value):
    status = 0
    try:
        value = int(value)
        print("{:d}".format(value), end="\n")
        return True
    except (TypeError, ValueError):
        return False
    return status
