#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
