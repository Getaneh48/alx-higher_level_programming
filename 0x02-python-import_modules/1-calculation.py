#!/usr/bin/python3
"""
a program that imports functions from the file
calculator_1.py, does some Maths, and prints the result
"""

from calculator_1 import add, sub, mul, div
a = 10
b = 5
if __name__ == '__main__':
    print(f"{a} + {b} = {add(a, b)}", end="\n")
    print(f"{a} - {b} = {sub(a, b)}", end="\n")
    print(f"{a} * {b} = {mul(a, b)}", end="\n")
    print(f"{a} / {b} = {div(a, b)}", end="\n")
