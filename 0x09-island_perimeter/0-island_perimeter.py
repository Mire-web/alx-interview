#!/usr/bin/python3
"""
Solving the island perimeter challenge in python
using DFS
"""
def island_perimeter(grid):
    """ Calculate Island Perimeter """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(row):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                if row < len(grid) and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col > 0 and grid[row][col - 1]:
                    perimeter -= 1
                if col < len(grid[0]) and col > grid[row][col + 1]:
                    perimeter -= 1
    return perimeter * 2

