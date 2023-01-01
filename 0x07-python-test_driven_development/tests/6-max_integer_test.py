"!/usr/bin/python3

import unittest

class MaxIntegerTest(unittest.TestCase):
    def test_Maximum(self):
        self.assertEqual([1, 2, 3, 4, 5], 5)
    def test_maximum2(self):
        self.assertEqual([-5, 0, 1,5], 5)
    def test_empty_list(self):
        self.assertEqual([], None)
    def test_list_with_empty_string(self):
        self.assertEqual([''], '')
    def test_list_with_one_int(self):
        self.assertEqual([20], 20)
    def test_list_shouldnt_contain_str(self):
        with self.assertRaises(TypeError):
            [10, 'fhdh']
    def test_list_shouldnt_be_none(self):
        with self.assertRaises(TypeError)
            None

    if __name__ == '__main__':
        unittest.main()

