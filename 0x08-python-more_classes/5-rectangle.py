#!/usr/bin/python3
"""
This module contains the class Rectangle.
"""


class Rectangle:
    """This class defines a rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This method returns the width of the rectangle.
        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This method sets the width of the rectangle.
        Args:
            value: The width of the rectangle.
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        This method returns the height of the rectangle.
        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This method sets the height of the rectangle.
        Args:
            value: The height of the rectangle.
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        This method returns the area of the rectangle.
        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        This method returns the perimeter of the rectangle.
        Returns:
            The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        This method returns a string representation of the rectangle.
        Returns:
            A string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """
        This method returns a string representation of the rectangle.
        Returns:
            A string representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        This method deletes the rectangle.
        Returns:
            None
        """
        print("Bye rectangle...")
