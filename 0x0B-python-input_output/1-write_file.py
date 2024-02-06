#!/usr/bin/python3
"""
write_file: writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file
    """
    with open(filename, 'w', encoding='utf-8') as write_txt:
        output = write_txt.write(text)
        return len(text)
