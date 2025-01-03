#!/usr/bin/python3
"""
Module: Square

this module contains a class definition for Square
"""


class Square:
    """
    A class to represent a Square.
    Attributes:
    size(int): The size of the Square. must be
    a non-negative integer.
    """
    def __init__(self, size=0):
        """
        Initialize a new instance of the Square class.

        Args:
            size(int): The size of the Square(default = 0).
        Raises:
            TypeError: if size not an integer
            ValueError: if size is negative
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
