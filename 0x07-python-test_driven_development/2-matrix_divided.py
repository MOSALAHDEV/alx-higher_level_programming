#!/usr/bin/python3
"""
This module contains a function that divides elements of matrix by a number
The function checks if the matrix is a list of lists of integers or flaots
checks if the lists of matrix of the same length
Functions:
    matrix_divided(matrix, div): divides each element of the matrix by div
Exceptions:
    TypeError and ZeroDivisionError
"""


def matrix_divided(matrix, div):
    """
    divides all elements of matrix by div
    args:
        matrix(list of lists)
        div(int or float)
    Return:
        new matrix with each element divided by div
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if not matrix:
        return []
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if element == float('inf') or element == float('-inf'):
                new_row.append(0.0)
            elif element != element:
                new_row.append(0.0)
            else:
                new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
