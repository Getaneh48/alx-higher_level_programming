#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    sum = 0
    for index, i in enumerate(sys.argv):
        if index == 0:
            continue
        sum = sum + int(i)

    print("{}".format(sum), end="\n")
