#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastDigit = abs(number) % 10
if number < 0:
    lastDigit = -lastDigit
if number % 10 > 5:
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
elif number % 10 == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0")
else:
    print(f"""Last digit of {number} is {lastDigit} \
and is less than 6 and not 0""")
