#!/usr/bin/python3
"""Base class ig"""
import json
from os import path


class Base:
    """This is a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON list representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            objs = []
        else:
            objs = [lists.to_dictionary() for lists in list_objs]
        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(objs))
