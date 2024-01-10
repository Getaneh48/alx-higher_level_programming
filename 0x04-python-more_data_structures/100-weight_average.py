#!/usr/bin/python3
"""
a function that returns the weighted average of all
integers tuple (<score>, <weight>)
"""

# my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = n2 = 0
    for k, x in my_list:
        sum += (k * x)
        n2 += x
    return sum / n2
