#!/usr/bin/python3
ignore = [ord('q'), ord('e')]
for i in range(97, 123):
    if i not in ignore:
        print("{}".format(chr(i)), end="")
