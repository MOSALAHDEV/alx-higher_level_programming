#!/usr/bin/python3
"""
This module contains the function text_indentation.
"""


def text_indentation(text):
    """this function prints a text with 2 new lines
    after each of these characters: ., ? and :
    there is no space after or before each line
    Args:
        text: text to print
    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    print(result, end='')
