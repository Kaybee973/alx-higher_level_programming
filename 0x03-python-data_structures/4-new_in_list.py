#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    original = list(my_list)
    if 0 <= idx < len(my_list):
        original[idx] = element
    return original
