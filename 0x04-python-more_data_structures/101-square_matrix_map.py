#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_mat = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
    return new_mat
