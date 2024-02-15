#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_init_size(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5, "expected 5")

    def test_square_init_invalid_size_input(self):
        with self.assertRaises(TypeError):
            Square("5")
    def test_squre_init_invalid_x_input(self):
        with self.assertRaises(TypeError):
            Square(5, "2")

    def test_square_size_value(self):
        with self.assertRaises(ValueError):
            Square(-2, 2)
        with self.assertRaises(ValueError):
            r = Square(2, 2)
            r.size = -10
        with self.assertRaises(ValueError):
            r = Square(2, 2)
            r.size = 0

    def test_square_update_by_args(self):
        s = Square(5, 3, 3)
        s.update(3, 10, 2, 2)
        self.assertEqual(s.size, 10, "expected 10")
        self.assertEqual(s.x, 2, "expected 2")
        self.assertEqual(s.y, 2, "expected 2")

    def test_square_update_by_kwargs(self):
       s = Square(5, 3, 3)
       s.update(size=20, x=4, y=3)
       self.assertEqual(s.size, 20, "expected 20")
       self.assertEqual(s.x, 4, "expected 4")
       self.assertEqual(s.y, 3, "expected 3")

    def test_square_to_dictionary(self):
       s = Square(3, 5, 3, 3)
       self.assertEqual(s.to_dictionary(), {'id': 3, 'size': 3, 'x': 5, 'y': 3}, "expected {'id': 3, 'size': 3, 'x': 5, 'y': 3}")
