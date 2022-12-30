#!/usr/bin/python3

"""
    checks if a matrix is alists of list
"""


def check_matrix_is_listoflist(matrix):
    valid = True
    if len(matrix) > 0:
        for m in matrix:
            if type(m) is not list:
                valid = False
                break
    return valid


"""
    checks if the list of a matrix has equal length
"""


def check_row_length_equality(matrix):
    valid = True
    row_len = len(matrix[0])
    for m in matrix:
        if len(m) != row_len:
            valid = False
            break
    return valid


"""Check if elements of the matrix row are int or float"""


def check_row_element_types(matrix):
    valid = True
    for m in matrix:
        for e in m:
            if type(e) is not int and type(e) is not float:
                valid = False
                break

    return (valid)


"""a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    divides each element of a matrix by a given number.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    if not check_matrix_is_listoflist(matrix):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if not check_row_length_equality(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not check_row_element_types(matrix):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [list(map(lambda e: round(e / div, 2), m)) for m in matrix]

    return result
