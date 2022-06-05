#!/usr/bin/python3
def element_at(my_list, idx):
    if 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        return None

lst = [10,2,4,7,8]
print(element_at(lst, 6))