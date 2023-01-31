#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Square: Class corresponding to a square"""
    def __init__(self, size):
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise Exception ValueError("size must be >= 0")