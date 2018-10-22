#!/usr/bin/python3
"""
unit tests for square module
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    test cases for square
    """

    def test_createsquare(self):
        new = Square(2, 2, id=60)
        self.assertEqual(str(new), '[Square] (60) 2/0 - 2')

    def test_size(self):
        new = Square(6)
        self.assertEqual(new.size, 6)
        self.assertEqual(new.width, 6)

    def test_no_size(self):
        with self.assertRaises(TypeError):
            new = Square()

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            new = Square(-8)

    def string_as_input(self):
        with self.assertRaises(TypeError):
            new = Square("Danny")

    def list_as_input(self):
        with self.assertRaises(TypeError):
            new = Square([1, 2, 3])

    def tuple_as_input(self):
        with self.assertRaises(TypeError):
            new = Square((6, 7))

    def dict_as_input(self):
        with self.assertRaises(TypeError):
            new = Square({'size': 30})

    def test_x_values(self):
        square1 = Square(2, 3, 4, 78)
        square2 = Square(5, 6, 1, 45)
        square3 = Square(9, 2, 7, 98)
        square4 = Square(5, 8, 9, 44)
        square5 = Square(1, 9, 5, 77)
        self.assertEqual(square1.x, 3)
        self.assertEqual(square2.x, 6)
        self.assertEqual(square3.x, 2)
        self.assertEqual(square4.x, 8)
        self.assertEqual(square5.x, 9)

    def test_y_values(self):
        square1 = Square(2, 3, 4, 78)
        square2 = Square(5, 6, 1, 45)
        square3 = Square(9, 2, 7, 98)
        square4 = Square(5, 8, 9, 44)
        square5 = Square(1, 9, 5, 77)
        self.assertEqual(square1.y, 4)
        self.assertEqual(square2.y, 1)
        self.assertEqual(square3.y, 7)
        self.assertEqual(square4.y, 9)
        self.assertEqual(square5.y, 5)

    def test_update(self):
        new = Square(1, 2, 3, 4)
        new.update(5, 6, 7, 8)
        self.assertEqual(new.id, 5)
        self.assertEqual(new.size, 6)
        self.assertEqual(new.x, 7)
        self.assertEqual(new.y, 8)
