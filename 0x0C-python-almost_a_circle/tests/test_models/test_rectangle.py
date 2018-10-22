#!/usr/bin/python3
"""
tests for Rectangle Class
"""

import unittest
import json
from models import rectangle
from models.rectangle import Rectangle
from models.base import Base


class TestRect(unittest.TestCase):
    """
    tests for class rectangle
    """
    def test_rectid(self):
        r1 = Rectangle(1, 2, 3, 4, 988)
        self.assertEqual(r1.id, 988)

    def test_width(self):
        i = Rectangle(2, 2)
        new = i.width
        self.assertEqual(new, 2)

    def test_height(self):
        i = Rectangle(3, 3)
        new = i.height
        self.assertEqual(new, 3)

    def test_x(self):
        i = Rectangle(6, 7, 6)
        new = i.x
        self.assertEqual(new, 6)

    def test_y(self):
        i = Rectangle(8, 8, 8, 8)
        new = i.y
        self.assertEqual(new, 8)

    def test_height_error(self):
        with self.assertRaises(TypeError):
            i = Rectangle(1)

    def test_width_error(self):
        with self.assertRaises(TypeError):
            i = Rectangle()

    def test_x_error(self):
        with self.assertRaises(TypeError):
            i = Rectangle(1, 2, "y", 5)

    def test_y_error(self):
        with self.assertRaises(TypeError):
            i = Rectangle(1, 2, 3, "four")

    def test_area(self):
        i = Rectangle(10, 4)
        new = i.area()
        self.assertEqual(new, 40)

    def test_update_id(self):
        i = Rectangle(5, 6, 7)
        i.update(8)
        self.assertEqual(i.id, 8)

    def test_update_height(self):
        i = Rectangle(3, 4, 5, 6)
        i.update(1, 2, 8, 9)
        self.assertEqual(i.height, 8)

    def test_update_width(self):
        i = Rectangle(4, 5, 6, 6)
        i.update(1, 2, 3, 4)
        self.assertEqual(i.width, 2)
