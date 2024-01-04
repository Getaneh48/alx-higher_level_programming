#!/usr/bin/python3
"""
a program that prints all the names defined by
the compiled module hidden_4.pyc
"""
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for n in names:
        if n[:2] != "__":
            print(f"{n}", end="\n")
