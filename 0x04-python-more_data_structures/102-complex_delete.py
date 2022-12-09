#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ids = [k for k, v in a_dictionary.items() if v == value]
    for i in ids:
        del a_dictionary[i]

    return a_dictionary
