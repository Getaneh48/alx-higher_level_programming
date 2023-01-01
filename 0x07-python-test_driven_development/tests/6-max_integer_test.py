#!/usr/bin/python3

"""unit test of max_integer function"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class MaxIntegerTest(unittest.TestCase):
    def test_Maximum(self):
        """test for the maximum of a list of integer"""

        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_maximum2(self):
        """test for the maximum of a list of integer"""

        self.assertEqual(max_integer([-5, 0, 1, 5]), 5)

    def test_float_values(self):
        """tests for maximum of float and int values"""

        self.assertEqual(max_integer([-3, 3, 5.6, -2.3]), 5.6)

    def test_empty_list(self):
        """test for empty list"""

        self.assertEqual(max_integer([]), None)

    def test_list_with_empty_string(self):
        """test for a list with one empty string"""

        self.assertEqual(max_integer(['']), '')

    def test_list_with_one_int(self):
        """tests for a list with one integer value"""

        self.assertEqual(max_integer([20]), 20)

    def test_list_shouldnt_contain_str(self):
        """tests for a list containing invalid value"""

        with self.assertRaises(TypeError):
            max_integer([10, 'fhdh'])

    def test_list_shouldnt_be_none(self):
        """tests for a None value"""

        with self.assertRaises(TypeError):
            max_integer(None)

    if __name__ == '__main__':
        unittest.main()
