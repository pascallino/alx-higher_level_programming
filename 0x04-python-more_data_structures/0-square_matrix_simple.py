#!/usr/bin/python3
def square_matrix_simple(matrix=[[]]):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return
    elif not matrix:
        return
    else:
        newMat = list([ele * ele for ele in row] for row in matrix)
        return newMat
