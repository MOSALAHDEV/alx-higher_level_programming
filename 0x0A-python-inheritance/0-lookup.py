#!/usr/bin/python3
def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    if obj is None:
        return None
    return dir(obj)
