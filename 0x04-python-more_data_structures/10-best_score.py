#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return 'none'

    max = 0
    for k, v in a_dictionary.items():
        if v > max:
            max = v

    ind = list(a_dictionary.values()).index(max)
    key = list(a_dictionary.keys())[ind]
    return key
