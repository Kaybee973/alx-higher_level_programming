#!/usr/bin/python3
for alpha in range(122, 96, -1):
    print(chr(alpha) if alpha % 2 ==0 else  chr(alpha - 32))