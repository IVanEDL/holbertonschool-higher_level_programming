#!/usr/bin/python3
"""Task 1"""


def write_file(filename="", text=""):
    """Writes a file."""
    with open(filename, 'w', encoding='utf-8') as i:
        return i.write(text)
