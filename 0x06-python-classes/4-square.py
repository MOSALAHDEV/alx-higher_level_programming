#!/usr/bin/python3
"""
Module: Square

This module contains a class definition for a square.
The Square class defines a square with a given size, providing methods
for initialization, area claculation, and validation of the size attribute.
"""


class Square:
    """
    A class to represent a Square.
    Attributes:
        size (int): The size of the square must be a non-negative integer.

    Methods:
        __init__(size=0):
            initialize the Square with the given size.
        area():
            Returns the area of the square.
        size():
            getter for the size attribute.
        size(value):
            setter to update the size attribute.
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

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Gets the size of the Square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        args:
            value (int): the new size of the square.

        Raises:
            TypeError: if size not an integer.
            ValueError: if size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
