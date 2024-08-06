#!/usr/bin/env python3
"""
Test Subtract Module

This module contains unit tests for the subtract function.
"""

import unittest
from operations.subtract import subtract


class TestSubtract(unittest.TestCase):
    """
    Contains unit tests for the subtract function.
    """

    def test_subtract(self):
        """
        Tests the subtract function with various inputs.
        """
        self.assertEqual(subtract(10, 5), 5, "Should be 5")
        self.assertEqual(subtract(-1, 1), -2, "Should be -2")
        self.assertEqual(subtract(-1, -1), 0, "Should be 0")
        self.assertEqual(subtract(0, 0), 0, "Should be 0")


if __name__ == "__main__":
    unittest.main()
