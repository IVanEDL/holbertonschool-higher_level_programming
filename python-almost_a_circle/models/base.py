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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) is 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            clas = cls(1, 1)
        else:
            clas = cls(1)
        clas.update(**dictionary)
        return clas

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        if not path.exists(f"cls.__name__".json):
            return []
        with open(f"{cls.__name__}.json", encoding='utf-8') as f:
            lists = []
            for dirks in cls.from_json_string(f.read()):
                dirks.append(cls.create(**dirks))
        return lists
