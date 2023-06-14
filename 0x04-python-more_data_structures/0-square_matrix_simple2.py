#!/usr/bin/python3
def square_matrix_simple(matrix=[[]]):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return
    elif not matrix:
        return
    else:
        newMat = []
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        newMat =[]
        for i in range(0, num_rows):
            newMat.append([])
        for row in newMat:
            for j in range(0, num_cols):
                row.append(None)
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                newMat[i][j] = col * col
        return newMat
