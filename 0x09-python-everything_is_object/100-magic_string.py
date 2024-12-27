#!/usr/bin/python3
def magic_string():
    magic_string.l = getattr(magic_string, "l", 0) + 1
    return ", ".join(["BestSchool"] * magic_string.l)
