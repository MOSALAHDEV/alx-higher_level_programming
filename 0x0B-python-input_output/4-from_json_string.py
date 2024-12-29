#!/usr/bin/python3
"""
This module contains the function from_json_string
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string
    Args:
        my_str: JSON string
    Returns:
        Object represented by the JSON string
    """
    return json.loads(my_str)
