#!/usr/bin/python3
"""TASK 9"""


class Student:
    """Class of a student that studes y studo"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary description of self"""
        if attrs is None:
            return self.__dict__
        return {a: i for a, i in self.__dict__.items() if a in attrs}

    def reload_from_json(self, json):
        """replaces all attributes from student instance"""
        if len(json) > 0:
            self.first_name = json.get('first_name')
            self.last_name = json.get('last_name')
            self.age = json.get('age')
