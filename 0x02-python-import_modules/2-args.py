#!/usr/bin/python3
"""
a program that prints the number of and the list
of its arguments.
"""
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print(f"0 arguments.", end="\n")
    elif len(sys.argv) == 2:
        print(f"1 argument:", end="\n")
        print(f"1: {sys.argv[1]}", end="\n")
    else:
        print(f"{len(sys.argv) - 1} arguments:", end="\n")
        for i in range(0, len(sys.argv)):
            if i == 0:
                continue
            print(f"{i}: {sys.argv[i]}", end="\n")
