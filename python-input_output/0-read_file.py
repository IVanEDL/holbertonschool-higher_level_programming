#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """Reads a file."""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
