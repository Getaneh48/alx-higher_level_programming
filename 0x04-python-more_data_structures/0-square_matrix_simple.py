#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(lambda n:n ** 2, lst)) for lst in matrix]
    return new_matrix
