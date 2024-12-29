#!/usr/bin/python3
"""
This module contains the function write_file.
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file
    Args:
        filename: name of the file
        text: text to write
    Returns:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
