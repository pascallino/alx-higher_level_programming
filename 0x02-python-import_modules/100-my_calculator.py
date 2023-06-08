#!/usr/bin/python3
import sys

from builtins import IndexError

if __name__ == '__main__':
    opt = ['+', '-', '*', '/']
    if not len(sys.argv) >= 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif len(sys.argv) >= 4:
        if not sys.argv[2] in opt:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    ch = sys.argv[2]
    exp = f"{a} {ch} {b}"
    res = eval(exp)
    print("{} {} {} = {}".format(a, ch, b, res))
