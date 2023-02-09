#!/usr/bin/python3
"""indents a text given a ., ? or :"""


def text_indentation(text):
    """prints a text with 2 new lines after some given characters"""
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in {'?', ':', '.'}:
            print("\n")
            while text[i + 1] == ' ':
                i += 1
        i += 1
