#!/usr/bin/python3
"""prints a square given by size"""


def print_square(size):
    """Function that prints a square. Checks for errors"""
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for p in range(size):
            print("#", end="")
        print("")
