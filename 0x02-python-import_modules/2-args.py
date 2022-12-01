#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) > 1:
        print("{} arguments:".format(len(sys.argv) - 1), end="\n")
        for index, i in enumerate(sys.argv):
            if index == 0:
                continue
            print("{}: {}".format(index, sys.argv[index]), end="\n")
