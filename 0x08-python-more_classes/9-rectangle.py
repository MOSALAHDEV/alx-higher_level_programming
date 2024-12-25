#!/usr/bin/python3
"""
This module contains the class Rectangle.
"""


class Rectangle:
    """This class defines a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        a = str(self.print_symbol)
        lines = [a * self.width for _ in range(self.height)]
        return "\n".join(lines)

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
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This method returns the biggest rectangle based on the area.
        Args:
            rect_1: The first rectangle.
            rect_2: The second rectangle.
        Returns:
            The biggest rectangle based on the area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        This method returns a square.
        Args:
            size: The size of the square.
        Returns:
            A square.
        """
        return cls(size, size)
