#!/usr/bin/python3
"""Task 12. Oh man."""


def pascal_triangle(n):
    """does the pascal triangly thing"""
    if n <= 0:
        return []
    else:
        triangle = [[1]]
    for i in range(1, n - 1):
        aux = [1]
        for p in range(1, i + 1):
            aux.append(triangle[i][p] + triangle[i][p - 1])
        aux.append(1)
        triangle.append(aux)
    return triangle
