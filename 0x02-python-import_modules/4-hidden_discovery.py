#!/usr/bin/python3
import sys
import hidden_4
if __name__ == "__main__":
    pass
sys.path.append(r"C:\Users\doc4.208\Downloads")
for arg in dir(hidden_4):
    if arg[:2] != "__":
        print(arg)
