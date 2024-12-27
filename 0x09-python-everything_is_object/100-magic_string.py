#!/usr/bin/python3
def magic_string():
    count = getattr(magic_string, 'count', 0)
    setattr(magic_string, 'count', count + 1)
    return "BestSchool, " * (count) + "BestSchool"
