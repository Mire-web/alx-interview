#!/usr/bin/python3
"""
Description: Implementation of pascal's Triangle in python
Author: Mirey_dev (mire-web)
"""


def pascal_triangle(n):
    """
    Handle Pascal triangle Generation
    return: Array representaing Pascal's triangle
    """
    if n <= 0:
        return []
    row_count = 0
    the_triangle = []
    while row_count < n:
        row = []
        if row_count == 0:
            row.append(1)
        else:
            for idx in range(row_count + 1):
                # Add 1 to start and end of row
                if idx == 0 or idx == row_count:
                    row.append(1)
                else:
                    # Get Current index in previous row
                    current_index = the_triangle[row_count - 1][idx]
                    # Get previous index in previous row
                    previous_index = the_triangle[row_count - 1][idx - 1]
                    new_number = current_index + previous_index
                    row.append(new_number)
        # Add row to triangle base
        the_triangle.append(row)
        row_count += 1
    return the_triangle