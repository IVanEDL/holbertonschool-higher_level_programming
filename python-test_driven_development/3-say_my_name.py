#!/usr/bin/python3
"""
prints the name given
"""

def say_my_name(first_name, last_name=""):
    """
    prints a string conformed of the given parts, first checking for
    strings
    """
    if not first_name or isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    elif isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
