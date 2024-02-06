#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""


import sys

if __name__ == "__main__":

    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file =\
        __import__("6-load_from_json_file").load_from_json_file

    arg_len = len(sys.argv)

    filename = "add_item.json"
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    for i in range(1, arg_len):
        my_list.append(sys.argv[i])

    save_to_json_file(my_list, filename)
