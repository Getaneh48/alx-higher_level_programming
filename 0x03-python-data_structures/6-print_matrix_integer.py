#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print("", end="\n")
        return
    for m in matrix:
        for ind, i in enumerate(m):
            if ind < len(m) - 1:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i))
