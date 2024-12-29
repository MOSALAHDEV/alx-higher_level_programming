#!/usr/bin/python3
"""
This module contains the function to_json_string
"""


import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object
    Args:
        my_obj: object to convert to JSON
    Returns:
        JSON representation of the object
    """
    return json.dumps(my_obj)
