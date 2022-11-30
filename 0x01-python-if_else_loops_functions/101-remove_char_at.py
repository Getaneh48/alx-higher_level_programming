#!/usr/bin/python3


def remove_char_at(str, n):
    index = 0
    for c in str:
        if index != n:
            print("{}".format(c), end="")
        index = index + 1

    return ""
