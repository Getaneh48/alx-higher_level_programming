#!/usr/bin/python3
"""a class that inherits from a base class 'list'"""


class MyList(list):
    """a class that inherits from a base class list"""

    def print_sorted(self):
        # prints the list, but sorted (ascending sort)

        print(sorted(self))
