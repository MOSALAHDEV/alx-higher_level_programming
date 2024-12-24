#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertTrue(max_integer([1, 2, 3, 4]) == 4)
        self.assertFalse(max_integer([1, 2, 3, 4]) == 3)
    def test_isinstance(self):
        self.assertIsInstance(max_integer([1, 2, 3, 4]), int)
        self.assertIsInstance([1, 2, 3, 4], list)
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
        self.assertFalse(max_integer([]))
    def test_negative_list(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertTrue(max_integer([-1, -2, -3, -4]) == -1)
        self.assertFalse(max_integer([-1, -2, -3, -4]) == -2)
if __name__ == '__main__':
    unittest.main()
