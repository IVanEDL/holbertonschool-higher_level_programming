#!/usr/bin/python3
"""TASK 5"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a file in a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as a:
        a.write(json.dumps(my_obj))
