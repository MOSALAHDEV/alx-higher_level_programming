#!/usr/bin/python3
""" This module contains the class MyList """


class MyList(list):
    """ This class inherits from list """
    def print_sorted(self):
        """ This function prints the list sorted """
        print(sorted(self))
