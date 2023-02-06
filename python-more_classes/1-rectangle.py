#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """yes. Rectangle."""
    def __init__(self, width=0, height=0):
        """initialization method. Cash and money."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.width

    @property
    def height(self):
        """height getter"""
        return self.height

    @width.setter
    def width(self, width):
        """width setter"""
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """height setter"""
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
