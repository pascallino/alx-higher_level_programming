#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        div = a/b
    except (ZeroDivisionError, TypeError, ValueError):
        div = None
        return div
    finally:
        print("Inside result: {}".format(div))
        return div
