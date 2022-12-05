#!/usr/bin/python3


def is_d(n):
    if n % 2 == 0:
        return (True)
    else:
        return (False)


def divisible_by_2(my_list=[]):
    return ([is_d(i) for i in my_list])
