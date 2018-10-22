#!/usr/bin/python3
"""
tests for base
"""

import unittest
import json
from models.base import Base
from models import base


class Test_Docs(unittest.TestCase):
    """
    documentation tests
    """
    def test_all_methods(self):
        for i in dir(Base):
            self.assertTrue(len(i.__doc__) > 0)

    def test_file_docs(self):
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_docs(self):
        self.assertTrue(len(Base.__doc__) > 0)


class Test_Base(unittest.TestCase):
    """
    checks if base class works properly
    """
    def test_id(self):
        base1 = Base(4)
        base2 = Base(12)
        base3 = Base(56)
        base4 = Base()
        base5 = Base()
        self.assertEqual(base1.id, 4)
        self.assertEqual(base2.id, 12)
        self.assertEqual(base3.id, 56)
        self.assertEqual(base4.id, 1)
        self.assertEqual(base5.id, 2)

    def test_id_as_string(self):
        b = Base("Daniel")
        self.assertEqual(b.id, "Daniel")

    def test_json(self):
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')
        dict = {'x': 6, 'y': 7, 'width': 2, 'height': 6, 'id': 12}
        to_json = Base.to_json_string(dict)
        to_dict = json.loads(to_json)
        self.assertEqual(type(to_json), str)
        self.assertEqual(to_dict, dict)
