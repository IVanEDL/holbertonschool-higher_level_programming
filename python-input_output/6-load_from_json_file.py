#!/usr/bin/python3
"""TASK 6"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, encoding='utf-8') as p:
        return json.load(p)
