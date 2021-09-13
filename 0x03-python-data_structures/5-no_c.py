#!/usr/bin/python3
def no_c(my_string):
    str1 = ""
    size = len(my_string)
    for x in range(0, size):
        if(my_string[x] != "C" and my_string[x] != "c"):
            str1 = str1 + my_string[x]
    return(str1)
