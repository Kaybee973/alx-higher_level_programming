#!/usr/bin/python3
def infinite_add(argv):
    num = len(argv)
    if num > 1:
        i = 1
        a = 0
        while i < (num):
            a += int(argv[i])
            i += 1
        print("{:d}".format(a))
    else:
        print("{:d}".format(num - 1))
if __name__ == '__main__':
    import sys
    infinite_add(sys.argv)