#!/usr/bin/python3
"""
defines a base a class
"""

import json
import os


class Base:
    """
    a base class for all child classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor

        Args:
            self: class instance
            id: int
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        a static method given a dictionery, returns a json string representation

        Args:
            list_dictionaries(list): list of dictionaries
        Returns:
            str: Json string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of lists_objs to a file

        Args:
            list_objs(list): list of objects
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                ls = []
                for obj in list_objs:
                    ls.append(obj.to_dictionary())
                f.write(cls.to_json_string(ls))

    def from_json_string(json_string):
        """
        given JSON string, returns a list of the JSON string representation

        Args:
            json_string(str): json string
        Returns:
            list: JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        given a dictionary of attributes, returns an instance with all attributes already set

        Args:
            dict: dictionary of attributes
        Returns:
            an instance all attributes set based on the dictionary values
        """
        if cls.__name__ == 'Rectangle':
            rec = cls(1, 1, 1, 1)
            rec.update(**dictionary)
            return rec
        elif cls.__name__ == 'Square':
            sqr = cls(2, 2, 2)
            sqr.update(**dictionary)
            return sqr

    @classmethod
    def load_from_file(cls):
        """
        returns a lists of instances from a given file

        Returns:
            list: list of instances
        """
        filename = cls.__name__+'.json'
        if not os.path.isfile(filename):
            return []
        instances = []
        with open(filename, 'r') as f:
            obj_text = f.read()
            obj = cls.from_json_string(obj_text)
            for o in obj:
                inst = cls.create(**o)
                print(inst)
                instances.append(inst)
        return instances
