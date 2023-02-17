#!/usr/bin/python3
"""File corresponding to the square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        super().__init__(self.__size, self.__size, x, y, id)

    def __str__(self):
        """str return method"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} "
                f"- {self.height}")
