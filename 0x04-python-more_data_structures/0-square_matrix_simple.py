#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMat = []
    rowPos = 0
    for row in matrix:
        newMat.append([])
        for item in row:
            newMat[rowPos].append(item ** 2)
        rowPos += 1
    return newMat
