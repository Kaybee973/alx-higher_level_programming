#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    num = len(sys.argv)
    if num > 1:
        i = 1
        a = 0
        while i < (num):
            a += int(sys.argv[i])
            i += 1
        print("{:d}".format(a))
    else:
        print("{:d}".format(num - 1))