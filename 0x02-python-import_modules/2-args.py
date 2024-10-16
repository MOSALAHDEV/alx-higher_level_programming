#!/usr/bin/python3
import sys
arguments = sys.argv[1:]
number = len(arguments)
if number == 0:
    print("0 arguments")
elif number == 1:
    print("1 argument:")
    print("1: {}".format(arguments[0]))
else:
    print("{} arguments:".format(number))
    for i, argument in enumerate(arguments, start=1):
        print("{}: {}".format(i, argument))
if __name__ == "__main__":
    pass
