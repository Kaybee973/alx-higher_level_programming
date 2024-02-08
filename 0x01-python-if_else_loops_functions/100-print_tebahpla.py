#!/usr/bin/python3
for alpha in range(122, 96, -1):
    print("{:c}".format(alpha) if alpha % 2 ==0 else  "{}".format(chr(alpha - 32)), end="")