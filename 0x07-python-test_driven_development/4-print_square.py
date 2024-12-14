#!/usr/bin/python3
"""
Define a function print_square that prints a square with the character #
Function name: print_square
Prototype: def print_square(size):
size is the size length of the square
"""


def print_square(size):
    """
    Function that prints a square with the character #
    Args:
        size: size of the square
    Returns:
        None
    """
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size != size:
        TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
