#!/usr/bin/python3
"""TAsk 10: SQUARE"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square."""
    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        super().__init__(size, size)
