#!/usr/bin/python3
"""Task 2"""


def write_file(filename="", text=""):
    """Writes a file."""
    with open(filename, 'a', encoding='utf-8') as i:
        return i.write(text)
