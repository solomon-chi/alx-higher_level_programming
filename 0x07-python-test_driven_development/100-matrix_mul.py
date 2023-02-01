#!/usr/bin/python3
"""
    Write a function that multiplies 2 matrices:
    Read: Matrix multiplication - only Matrix product (two matrices)
    Prototype: def matrix_mul(m_a, m_b):
    m_a and m_b must be validated with these requirements in this order
    m_a and m_b must be an list of lists of integers or floats:
    1. if m_a or m_b is not a list: raise a TypeError exception
    with the message m_a must be a list or m_b must be a list
    2. if m_a or m_b is not a list of lists: raise a TypeError
    exception with the message m_a must be a list of lists or
    m_b must be a list of lists
    3. if m_a or m_b is empty (it means: = [] or = [[]]): raise
    a ValueError exception with the message m_a can't be empty
    or m_b can't be empty
    4. if one element of those list of lists is not an integer or
    a float: raise a TypeError exception with the message m_a
    should contain only integers or floats or m_b should
    contain only integers or floats
    5. if m_a or m_b is not a rectangle (all ▒~@~Xrows▒~@~Y should be
    of the same size): raise a TypeError exception with the
    message each row of m_a must be of the same size or
    each row of m_b must be of the same size
    6. If m_a and m_b can▒~@~Yt be multiplied: raise a ValueError
    exception with the message m_a and m_b can't be
    multiplied
    #a = [[3, 2, 1, 5], [9, 1, 3, 0]]
    #b = [[2, 9, 0], [1, 3, 5], [2, 4, 7], [8, 1, 5]]
    #print(mult(a, b))
    # 3x2
    #axb = [[60 60]]
"""


def transpose(matrix):
    """ transpose a matrix """
    new_matrix = []
    for column in matrix[0]:
        new_matrix.append([])
    for row in matrix:
        for index, item in enumerate(row):
            new_matrix[index].append(item)
    return new_matrix


def dot_product(row_a, row_b):
    """ multiply dot 2 matrix """
    sum = 0
    for index, item in enumerate(row_a):

