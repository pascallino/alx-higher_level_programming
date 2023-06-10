#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        print("{:s}".format(""))
    for item in matrix:
        for i in range(0, len(item)):
            if i < len(item) - 1:
                print("{:d} ".format(item[i]), end="")
            else:
                print("{:d}".format(item[i]))
