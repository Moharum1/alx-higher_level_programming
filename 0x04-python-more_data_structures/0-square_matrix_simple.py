#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMat = matrix.copy()

    for i,row in enumerate(matrix):
        newMat[i] = list(map(lambda x: x**2, row))

    return newMat
