#!/usr/bin/python3
"""
read_file: reads the file with .txt
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r', encoding='utf-8') as read_file:
        output = read_file.read()
        print(output, end="")
