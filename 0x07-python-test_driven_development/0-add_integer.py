#!/usr/bin/python3
"""
This module provides a function to add 2 integers
"""
def add_integer(a, b=98):
    """
    add_integer adds 2 integers a and b
    if a and b are floats it casts them to integers before adding
    if a and b are not integers or floats it raises TypeError
    args:
        a: first number int or float
        b: second number int or float
    Returns:
        the sum of a and b as integers
    raises:
        TypeError: if a and b not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    else:
        a
    if isinstance(b, float):
        b = int(b)
    else:
        b
    return a + b
