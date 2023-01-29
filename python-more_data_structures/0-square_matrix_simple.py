#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for elements in matrix:
        matrix2.append(list(map(lambda alpha: alpha ** 2, elements)))
    return matrix2
