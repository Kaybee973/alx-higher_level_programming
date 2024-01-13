#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    # My addition function
    print("{} + {} = {}".format(a, b, add(a, b)))

    #My subtraction function
    print("{} - {} = {}".format(a, b, sub(a, b)))

    #My multiplication function
    print("{} * {} = {}".format(a, b, mul(a, b)))

    #My division function
    print("{} / {} = {}".format(a, b, div(a, b)))
