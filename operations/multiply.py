#!/usr/bin/env python3
"""Multiplication Module"""

from typing import List


def multiply(args: List) -> float:
    """
    Multiply a list of numbers together and return the result.
    
    Parameters:
    args (List): A list of numbers to multiply.
    
    Returns:
    float: The result of multiplying all the numbers in the list.
    """
    value = 1
    for arg in args:
        arg = float(arg)
        if not isinstance(arg, (int, float)):
            raise ValueError("All arguments must be numbers.")
        value *= arg
    return value


def main():
    print("MULTIPLICATION")
    numbers = input("Enter the numbers you wish to multiply: ")
    print(multiply(numbers.split()))


if __name__ == "__main__":
    main()
