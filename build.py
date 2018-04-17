#!/usr/bin/env python3

import sys

prefix = ""

if len(sys.argv) == 2:
    prefix = sys.argv[1]

grid = [
    [2,0,0,6,7,1,0,0,0],
    [7,0,0,2,0,0,0,0,0],
    [0,0,0,5,0,0,0,0,0],
    [0,0,0,1,0,6,0,0,9],
    [4,7,1,0,5,0,0,0,0],
    [0,0,0,0,0,0,0,5,8],
    [0,0,0,0,0,2,6,0,0],
    [6,9,0,0,0,0,0,3,0],
    [5,0,0,0,6,3,0,7,0]
]

s = ""
for y in range(0, len(grid)):
    assert(len(grid) == len(grid[y]))
    for x in range(0, len(grid[y])):
        if (grid[y][x] > 0):
            assert(grid[y][x] <= len(grid))
            s += prefix + "s" + str(x) + "x" + str(y) + "x" + str(grid[y][x] - 1) + " := T;\n"

print(s)
