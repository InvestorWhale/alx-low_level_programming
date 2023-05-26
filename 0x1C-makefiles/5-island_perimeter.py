#!/usr/bin/python3
"""Module contains 'island_perimeter' function"""


def island_perimeter(grid):
    """
        Returns the perimeter described in grid
    """
    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                try:
                    if j == 0:
                        p += 1
                    else:
                        if grid[i][j-1] == 0:
                            p += 1
                except IndexError:
                    pass
                try:
                    if j == len(grid[i]) - 1:
                        p += 1
                    else:
                        if grid[i][j+1] == 0:
                            p += 1
                except IndexError:
                    pass
                try:
                    if i == 0:
                        p += 1
                    else:
                        if grid[i-1][j] == 0:
                            p += 1
                except IndexError:
                    pass
                try:
                    if i == len(grid) - 1:
                        p += 1
                    else:
                        if grid[i+1][j] == 0:
                            p += 1
                except IndexError:
                    pass
    return p
