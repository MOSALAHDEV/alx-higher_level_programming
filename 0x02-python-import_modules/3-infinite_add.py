#!/usr/bin/python3
import sys
numbers = sys.argv[1:]
x = 0
for number in numbers:
    x += int(number)
print(x)
if __name__ == "__main__":
    pass
