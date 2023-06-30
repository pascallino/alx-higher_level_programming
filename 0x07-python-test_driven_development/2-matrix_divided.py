#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix, list) and all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    result = list(map(lambda row: \
                      list(map(lambda x: x if isinstance(x, int) or \
                      isinstance(x, float) else \
                      TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats"), row)), matrix))
    rowlen = []
    for row in matrix:
        rowlen.append(len(row))
    if len(set(rowlen)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    result = list(map(lambda row: list(map(lambda x: \
                                           "{:.2f}".format(x / div), row)), matrix))
    return result
