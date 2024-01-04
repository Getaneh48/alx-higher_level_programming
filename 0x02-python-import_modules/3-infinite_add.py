#!/usr/bin/python3
"""
a program that prints the result of the addition of all arguments
"""
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("0", end="\n")
    else:
        sum = 0
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])
        print(f"{sum}", end="\n")
