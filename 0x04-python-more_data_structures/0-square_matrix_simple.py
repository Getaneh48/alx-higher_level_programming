#!/usr/bin/python3
"""
a function that computes the square value of all
integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
