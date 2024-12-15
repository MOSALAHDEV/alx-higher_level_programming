#!/usr/bin/python3
"""
This module contains the function text_indentation.
"""
def text_indentation(text):
    """this function prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text: text to print
    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in ".?:":
        text = text.replace(i, f"{i}\n")
    print(f"{text}", end="")
    print()
