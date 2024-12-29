#!/usr/bin/python3
"""
This module contains the function read_file.
"""


def read_file(filename=""):
    """
    Function that reads a text file and prints it to stdout
    Args:
        filename: name of the file to read
    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
