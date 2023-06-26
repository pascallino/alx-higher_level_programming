#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as e:
        sys.stderr.write("Exception: {}\n".format(str(e)))
        # print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
    except ValueError as e:
        sys.stderr.write("Exception: {}\n".format(str(e)))
        # print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
