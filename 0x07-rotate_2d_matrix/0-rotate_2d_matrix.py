#!/usr/bin/python3
"""
n x n 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    function that transposes and reverses a matrix
    """
    mat = len(matrix)

    for i in range(mat):
        for j in range(i, mat):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(mat):
        matrix[i].reverse()
