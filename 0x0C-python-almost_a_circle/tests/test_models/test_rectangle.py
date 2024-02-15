#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
import os

class TestRectangle(unittest.TestCase):
    def test_rectangle_init_two_args(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10, "Expected 10")
        self.assertEqual(r1.height, 2, "Expected 2")

    def test_rectangle_init_all_args(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12, "Expected 12")
    def test_rectangle_invalid_input(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_rectangle_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-2, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(2, 2)
            r.width = -2

    def test_rectangle_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_rectangle_height_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(2, -2)

    def test_rectangle_x_less_than_zero(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, -3, 1)


    def test_rectangle_y_less_than_zero(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, -1)

    def test_rectangle_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6, "Expected 6")

    def test_rectangle_area_with_all_args(self):
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56, "Expected 56")

    def test_rectangle_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6", "Expected [Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_update_args(self):
        r = Rectangle(3, 2)
        r.update(None, 2)
        self.assertEqual(r.width, 2, "Expected 10")

        r.update(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 1, "Expected 1")
        self.assertEqual(r.width, 2, "Expected 2")
        self.assertEqual(r.height, 3, "Expected 3")
        self.assertEqual(r.x, 4, "Expected 4")
        self.assertEqual(r.y, 5, "Expected 5")

    def test_rectangle_update_kwargs(self):
        r = Rectangle(3, 2)
        r.update(x=10, height=9)
        self.assertEqual(r.x, 10, "Expected 10")
        self.assertEqual(r.height, 9, "Expected 9")
        self.assertEqual(r.width, 3, "Expected 3")

    def test_rectangle_to_dictionary(self):
         r = Rectangle(4, 5, 2, 8, 10)
         self.assertEqual(r.to_dictionary(), {"x": 2, "y": 8, "id": 10, "width": 4, "height": 5}, 'Expected {"x": 2, "y": 8, "id": 10, "width": 4, "height": 5}')

    def test_rectangle_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists(Rectangle.__name__+".json"), "expected True")
        inst = Rectangle.load_from_file()
        self.assertEqual(len(inst), 2, "expected 2")
