#!/usr/bin/python3
"""task 2"""


def is_same_class(obj, a_class):
    """checks for same type of class"""
    return issubclass(a_class, type(obj))
