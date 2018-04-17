#!/usr/bin/env python3

import sys
assert(len(sys.argv) == 3)

f = open(sys.argv[2], 'r').read().split('\n')

size = int(sys.argv[1])

for prefix in ['s1', 's2', 's3', 's4', 's5']:
    grid = []
    for i in range(0, size):
        arr = [0] * size
        grid.append(arr[:])

    for l in f:
        if l[0:len(prefix)] == prefix:
            #print(l)
            l = l[len(prefix):]
            #print(l)
        else:
            continue

        if len(l) > 0 and l[0] == 's' and 'x' in l and ' == ' in l and 'T' in l:
            l_split = l[1:].split(' == ')
            l_var = l_split[0].split('x')
            if (len(l_var) != 3):
                print(l, l_var)
            assert(len(l_var) == 3)
            grid[int(l_var[1])][int(l_var[0])] = int(l_var[2])

    s = ""
    for y in range(0, size):
        for x in range(0, size):
            s += str(grid[y][x] + 1) + " "
        s += "\n"

    print(s)
