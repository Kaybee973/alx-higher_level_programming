#!/usr/bin/python3
"""
append_write:appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    """
    with open(filename, 'a', encoding='utf-8') as append:
        output = append.write(text)
        return len(text)
