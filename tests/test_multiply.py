#!/usr/bin/env python3
"""Multiplication Module Tests"""

import unittest

from operations.multiply import multiply


class TestMultiply(unittest.TestCase):
    """Multiplication Module Test Cases"""

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply([2, 3]), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply([-2, -3]), 6)
        self.assertEqual(multiply([-2, 3]), -6)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply([2, 0]), 0)

    def test_multiply_large_numbers(self):
        self.assertEqual(multiply([1000000, 1000000]), 1000000000000)

    def test_multiply_floating_point_numbers(self):
        self.assertEqual(multiply([2.5, 3]), 7.5)
        self.assertEqual(multiply([-2.5, -3.0]), 7.5)
        self.assertEqual(multiply([2.5, -3]), -7.5)

    def test_multiplicative_identity(self):
        self.assertEqual(multiply([5, 1]), 5)
        self.assertEqual(multiply([1, 5]), 5)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiply([4, 0.25]), 1)
        self.assertEqual(multiply([0.5, 2]), 1)

    def test_commutative_property(self):
        self.assertEqual(multiply([3, 5]), multiply([5, 3]))

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, multiply, ["Hello", "3"])

    def test_performance_large_inputs(self):
        import time
        start_time = time.time()
        multiply([10**100, 10**100])
        end_time = time.time()
        self.assertTrue((end_time - start_time) < 1,
                        "Performance test failed: took too long.")


if __name__ == '__main__':
    unittest.main()
