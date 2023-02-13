#!/usr/bin/python3
"""TASK 8"""


import json


def class_to_json(obj):
    """returns the dictionary description for json serialization of an obj"""
    return obj.__dict__
