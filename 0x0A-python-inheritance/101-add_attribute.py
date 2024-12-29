#!/usr/bin/python3
"""
Add a new attribute to an object if possible.

This function adds a new attribute to an object if it has a __dict__.
Otherwise, it raises a TypeError.
"""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object if possible.

    This function adds a new attribute to an object if it has a __dict__.
    Otherwise, it raises a TypeError.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
