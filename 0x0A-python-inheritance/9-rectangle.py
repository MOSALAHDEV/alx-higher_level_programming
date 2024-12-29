#!/usr/bin/python3
"""
This module contains the class Rectangle
which inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        This function initializes the class
        """
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        This function returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        This function returns the string representation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
