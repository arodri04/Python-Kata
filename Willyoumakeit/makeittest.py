#!/usr/bin/env python3

import unittest

from makeit import make_it

class TestMakeIt(unittest.TestCase):
  def test_true(self):
    self.assertEqual(make_it(25, 2, 50), True)

  def test_false(self):
    self.assertEqual(make_it(25, 2, 75), False)

  def test_string(self):
    self.assertEqual(make_it("25", 2, 75), "Enter mpg as a number")

# Run the tests
unittest.main()


