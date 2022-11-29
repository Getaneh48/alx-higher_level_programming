#!/usr/bin/python3

def p_letter(c, dlm):
    if ord(c) >= 97 and ord(c) <= 122:
        print("{}{}".format(chr(ord(c) - 32), dlm), end="")
    else:
        print("{}{}".format(c, dlm), end="")


def uppercase(str):
    for index, c in enumerate(str):
        if index == (len(str) - 1):
            p_letter(c, "\n")
        else:
            p_letter(c, "")
