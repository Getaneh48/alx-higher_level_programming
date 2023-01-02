#!/usr/bin/python3

"""a function that multiplies two matrixes"""


def matrix_mul(m_a, m_b):
    """returns the multiplication of two matrixes"""
    if not type(m_a) is list or not type(m_b) is list:
        raise TypeError("m_a must be a list or m_b must be a list")

    # check if the matrixes are valid
    for m in [m_a, m_b]:
        validate_matrix(m)

    # the number of rows of the second matrix
    fm_col_len = len(m_a[0])
    sm_row_len = len(m_b)

    if fm_col_len != sm_row_len:
        raise ValueError("m_a and m_b can't be multiplied")

    m2r = []
    for r in range(len(m_b[0])):
        m2r.append((list(map(lambda k: m_b[k][r], range(len(m_b))))))

    new_m = []
    for a_l in m_a:
        new_m.append([sum(list(map(lambda a, b: a * b, a_l, b_l)))
                     for b_l in m2r])

    return(new_m)


def validate_matrix(m):
    """check if the given matrix is valid"""

    if not type(m) is list:
        raise TypeError("m_a must be a list or m_b must be a list")
    for e in m:
        if not type(e) is list:
            raise TypeError("m_a must be a list of lists or m_b "
                            "must be a list of lists")

    # check if the matrix is emtpy
    if len(m) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    # check if the elements are not empty lists
    for e in m:
        if len(e) == 0:
            raise ValueError("m_a can't be empty or m_b can't be empty")

    # check if elements of the matrix are either int or float
    for e in m:
        for i in e:
            if not type(i) is int and not type(i) is float:
                raise TypeError("m_a should contain only integers or "
                                "floats or m_b should contain only "
                                "integers or float")

    # checks if the rows of the matrix are equal
    row_len = len(m[0])
    for e in m:
        if len(e) != row_len:
            raise TypeError("each row of m_a must be of the same size "
                            "or each row of m_b must be of the same size")
