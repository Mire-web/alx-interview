#!/usr/bin/python3
"""
Desc: A script to rotate a 2d matrix 90degrees clockwise
Author: Mirey_Dev
"""


def rotate_2d_matrix(matrix):
    size = len(matrix) - 1
    if size < 2:
        n = 1
    else:
        n = size // 2

    for i in range(n):
        for j in range(i, size-i):
            temp = matrix[size-j][i]
            matrix[size-j][i] = matrix[size-i][size-j]
            matrix[size-i][size-j] = matrix[j][size-i]
            matrix[j][size-i] = matrix[i][j]
            matrix[i][j] = temp
