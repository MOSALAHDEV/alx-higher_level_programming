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
        position():
            getter for the position attribute
        position(value):
            setter for the position attribute
        my_print():
            print the square using '#' character
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new instance of the Square class.

        Args:
            position(tuple): the square position
            size(int): The size of the Square(default = 0).
        Raises:
            TypeError: if size not an integer
            ValueError: if size is negative
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        sets the position of the square

        Returns: returns tuple that position the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the position of the square

        args:
            value (tuple): specifies the square position

            raises:
                TypeError
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints a square of size 'size' using the '#' character

        if size is zero prints an empty line
        """
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
