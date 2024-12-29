#!/usr/bin/python3
"""
This module contains the class Square that inherits from Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class inherits from Rectangle
    """
    def __init__(self, size):
        """
        This function initializes the class
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        This function returns the string representation of the square
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """
        This function returns the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        This function returns the string representation of the square
        """
        return f"[Square] {self.__size}/{self.__size}"
