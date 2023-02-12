#!/usr/bin/python3
"""Task 4"""


def inherits_from(obj, a_class):
    """Does the windy thing"""
    return isinstance(obj, a_class) and not issubclass(a_class, type(obj))
