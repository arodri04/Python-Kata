#!/usr/bin/env python3
import unittest
from binaryconvert import binaryconvert

class TestMakeIt(unittest.TestCase):
    def test_large(self):
      self.assertEqual(binaryconvert(1234), 5)
    def test_0(self):
      self.assertEqual(binaryconvert(0), 0)
    def test_9(self):
      self.assertEqual(binaryconvert(9), 2)

unittest.main()