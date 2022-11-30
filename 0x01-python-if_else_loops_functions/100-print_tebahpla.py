#!/usr/bin/python3

k = 0
for c in range(122, 96, -1):
    if k % 2 != 0:
        print("{}".format(chr(c - 32)), end="")
    else:
        print("{}".format(chr(c)), end="")
    k = k + 1
