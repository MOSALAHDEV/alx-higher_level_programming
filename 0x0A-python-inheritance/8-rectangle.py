#!/usr/bin/python3
"""
This module contains the class BaseGeometry.
"""


class BaseGeometry:
    """
    This class is empty
    """
    def area(self):
        """
        This function is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This class inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        This function initializes the class
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
