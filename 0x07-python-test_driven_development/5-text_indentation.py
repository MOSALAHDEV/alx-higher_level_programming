#!/usr/bin/python3
"""
This module contains the function text_indentation.
"""


def text_indentation(text):
    """this function prints a text with 2 new lines
    after each of these characters: ., ? and :
    Args:
        text: text to print
    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = []
    i = 0
    while i < len(text):
        result.append(text[i])
        if text[i] in ".?:":
            result.append("\n")
        while i + 1 < len(text) and text[i + 1] == ' ':
            i += 1
        i += 1
    result = ''.join(result)
    print(result)
