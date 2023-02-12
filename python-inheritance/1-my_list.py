#!/usr/bin/python3
"""Task 1"""


class MyList(list):
    """My list Class"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
