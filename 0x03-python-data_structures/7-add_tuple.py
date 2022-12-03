#!/usr/bin/python3


def fill_t(t):
    if len(t) == 0:
        return (0, 0)
    elif len(t) == 1:
        return (t[0], 0)
    else:
        return (t)


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = fill_t(tuple_a)
    tuple_b = fill_t(tuple_b)
    return ((tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]))
