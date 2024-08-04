#!/usr/bin/env python3
"""Power Module"""


def power(base, exponent):
    """
    Calculate the power of a number.
    :param base: The base number.
    :param exponent: The exponent to raise the base to.
    :return: The result of raising base to the power of exponent.
    """
    result = 1
    for _ in range(exponent):
        result *= base
    return result


if __name__ == "__main__":
    base = 2
    exponent = 3
    print(f"{base} raised to the power of
          {exponent} is {power(base, exponent)}")
