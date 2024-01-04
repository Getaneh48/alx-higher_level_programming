#!/usr/bin/python3
"""
a program that imports all functions from the file
calculator_1.py and handles basic operations
"""

from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <a> operator <b>", end="\n")
        sys.exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    match op:
        case "+":
            print(f"{a} + {b} = {add(a, b)}", end="\n")
        case "-":
            print(f"{a} - {b} = {sub(a, b)}", end="\n")
        case "*":
            print(f"{a} * {b} = {mul(a, b)}", end="\n")
        case "/":
            print(f"{a} / {b} = {div(a, b)}", end="\n")
        case _:
            print(f"Unknown operator. \
                  Available operators: +, -, * and /", end="\n")
            sys.exit(1)
