#!/usr/bin/env python3
"""
Subtract Module

This module provides a function to perform subtraction.
"""


def subtract(x, y):
    """
    Subtract the second number from the first number.

    Parameters:
    x (float): The number from which y will be subtracted.
    y (float): The number to subtract from x.

    Returns:
    float: The result of x - y.
    """
    return x - y


if __name__ == "__main__":
    x = 10
    y = 5
    print(f"The result of subtracting {y} from {x} is {subtract(x, y)}")
