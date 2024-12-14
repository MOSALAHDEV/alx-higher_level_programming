#!/usr/bin/python3
"""
This module prints first name and last name.
first name and last name must be strings
if not strings, raise TyepeError first_name must be
a string or last_name must be a string

function name say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints first name and last name.
    first name and last name must be strings
    if not strings, raise TyepeError first_name must be
    a string or last_name must be a string

    args:
        first_name(string)
        last_name(string)
    returns:
        a string with first and last name
    raises:
        TypeError: if first or last name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print(f"My name is {first_name} {last_name}")
    elif first_name is not None:
        print(f"My name is {first_name}")
    else:
        raise TypeError("first_name must be a string")
