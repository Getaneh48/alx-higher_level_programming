#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
import json

class TestBase(unittest.TestCase):
    def test_init_without_id(self):
        b = Base()
        self.assertEqual(b.id, 1, 'Expected 1')

    def test_init_with_id(self):
        b = Base(2)
        self.assertEqual(b.id, 2, 'Expected 2')

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), '[]', "should be empty list")

    def test_to_json_string_with_None_value(self):
        self.assertEqual(Base.to_json_string(None), '[]', "should be empty list")

    def test_to_json_string_with_single_dictionary_value(self):
        dct = {'x': 10, 'y': 20, 'width': 10, 'height': 5}
        self.assertEqual(Base.to_json_string(dct), '{"x": 10, "y": 20, "width": 10, "height": 5}', 'Expected \'{"x": 10, "y": 20, "width": 10, "height": 5}\'')

    def test_to_json_string_with_multiple_dictionary_value(self):
        ls = [{'x': 10, 'y': 20, 'width': 10, 'height': 5}, {'x': 3, 'y': 4, 'width': 6, 'height': 8}]
        self.assertEqual(Base.to_json_string(ls), '[{"x": 10, "y": 20, "width": 10, "height": 5}, {"x": 3, "y": 4, "width": 6, "height": 8}]')

    def test_save_to_file_objects(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Base.save_to_file([r1, r2])
        with open("Base.json", 'r') as file:
            js = json.load(file)
            self.assertEqual(len(js), 2, "Expected 2")

    def test_from_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dct = r1.to_dictionary()
        json_str = Base.to_json_string(dct)
        print(json_str, end="\n")
        js = Base.from_json_string(json_str)
        print(js)
        self.assertEqual(dct, js, "Expected True")

    def test_create(self):
       d = {'x': 10, 'y': 20, 'id': 1, 'width': 10, 'height': 5}
       r = Rectangle.create(**d)
       self.assertEqual(r.to_dictionary(), d, "Expected True")

