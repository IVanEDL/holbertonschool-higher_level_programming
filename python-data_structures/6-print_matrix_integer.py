#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for a in range(0, len(matrix[i])):
            print("{:d}".format(matrix[i][a]), end=" ")
        print("")
