#!/usr/bin/python3
import copy
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        copyList = copy.deepcopy(my_list)
        copyList[idx] = element
        return copyList
