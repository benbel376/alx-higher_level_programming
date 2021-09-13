#!/usr/bin/python3
replace = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_e = 9
newL = replace(my_list, idx, new_e)

print(newL)
print(my_list)
