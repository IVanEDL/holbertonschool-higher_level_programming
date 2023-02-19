#!/usr/bin/python3
"""File corresponding to the square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str return method"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} "
                f"- {self.height}")

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        self.width = size
        self.height = size
