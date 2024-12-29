#!/usr/bin/python3
"""
This module contains class MyInt  that inherits from int
"""


class MyInt(int):
    """ This class inherits from int"""
    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
