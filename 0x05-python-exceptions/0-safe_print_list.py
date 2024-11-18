#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end='')
            count += 1
    except IndexError:
        print()
        print("The number of element is out of range")
    finally:
        print()
    return count
