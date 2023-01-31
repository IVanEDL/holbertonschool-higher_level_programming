#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Square: Class corresponding to a square"""
    def __init__(self, size=0):
        """initializes method
        """
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """square getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """square setter"""
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """prints square"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for a in range(self.__size):
                print("#", end="")
            print("")
