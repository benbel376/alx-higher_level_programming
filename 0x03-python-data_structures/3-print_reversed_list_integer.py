#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    size = len(my_list) -1
    for x in range(size, -1, -1):
        print("{:d}\n".format(my_list[x]))
