#!/usr/bin/python3
"""Also divides a Matri but in big lmao"""


def matrix_divided(matrix, div):
    """Divides a Matri"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(0, len(matrix)):
        if i + 1 < len(matrix):
            if len(matrix[i]) != len(matrix[i+1]):
                raise TypeError("Each row of the matrix \
must have the same size")
        for p in range(0, len(matrix[i])):
            if type(matrix[i][p]) != int and type(matrix[i][p]) != float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    matrix2 = []
    for elements in matrix:
        matrix2.append(list(map(lambda alpha: alpha / div, elements)))
    return matrix2
