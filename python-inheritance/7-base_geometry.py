#!/usr/bin/python3
"""Base Geometry"""


class BaseGeometry:
    """Class of geometyr"""
    def area(self):
        """Does the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the integre"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
