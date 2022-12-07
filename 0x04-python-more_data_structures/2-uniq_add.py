#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for n in set(my_list):
        sum = sum + n

    return sum
