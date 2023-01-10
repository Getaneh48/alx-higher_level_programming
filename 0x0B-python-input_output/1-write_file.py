#!/usr/bin/python3
"""a file writting module"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns
       the number of characters written
    """

    with open(filename, mode='a') as f:
        f.write(text)
        return f.tell()
