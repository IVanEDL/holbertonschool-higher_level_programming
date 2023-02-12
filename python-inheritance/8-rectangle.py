#!/usr/bin/python3
"""Task 8"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """RECTANGOL class 2k23"""
    def __init__(self, width, height):
        """initialices class"""
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
