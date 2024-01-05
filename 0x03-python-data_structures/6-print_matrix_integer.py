#!/usr/bin/python3
"""
a function that prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print("{}".format(matrix[i][j]), end=" ")
        print(end="\n")
