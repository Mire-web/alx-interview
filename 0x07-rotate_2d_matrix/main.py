#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    mat = [[1, 3],
           [4, 5]]
    mat3 = [[1, 4, 6, 8],
            [3, 2, 5, 9],
            [5, 2, 1, 3],
            [4, 9, 7, 0]]

    rotate_2d_matrix(matrix)
    rotate_2d_matrix(mat)
    rotate_2d_matrix(mat3)
    rotate_2d_matrix([])
    print(matrix)
    print(mat)
    print(mat3)
