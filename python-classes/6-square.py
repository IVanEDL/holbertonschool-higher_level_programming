#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Square: Class corresponding to a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes method
        """
        self.__size = size
        self.__position = position
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if isinstance(position, tuple) is False or len(position) is not 2 or \
                not all(isinstance(az, int) and az >= 0 for az in position):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """returns area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """size setter"""
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """"position getter"""
        return self.__position

    @position.setter
    def position(self, position):
        """position setter"""
        self.__position = position
        if isinstance(position, tuple) is False or len(position) is not 2 or \
                not all(isinstance(az, int) and az >= 0 for az in position):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """prints square"""
        if self.__size == 0:
            print("")
            return
        for erin in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for p in range(self.__position[0]):
                print(" ", end="")
            for a in range(self.__size):
                print("#", end="")
            print("")
