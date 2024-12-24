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
    for i in ".?:":
        text = text.replace(i, f"{i}\n\n")
    modified_lines = [line.strip() for line in text.split("\n\n")]
    print("\n\n\n".join(modified_lines), end='')
