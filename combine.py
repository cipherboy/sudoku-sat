#!/usr/bin/env python

import sys

assert(len(sys.argv) == 10)

size = int(sys.argv[1])
p1 = sys.argv[2]
p1x_min = int(sys.argv[3])
p1x_max = int(sys.argv[4])+1
p1y_min = int(sys.argv[5])
p1y_max = int(sys.argv[6])+1
p2 = sys.argv[7]
p2x_min = int(sys.argv[8])
p2y_min = int(sys.argv[9])


f = open("50-combine-" + p1 + "-" + p2 + ".txt", "w")
c = 0

prefix = p1 + p2
combine = prefix + "combine := AND("
for p1x in range(p1x_min, p1x_max):
    for p1y in range(p1y_min, p1y_max):
        p2x = p2x_min + (p1x - p1x_min)
        p2y = p2y_min + (p1y - p1y_min)
        for v in range(0, size):
            combine += p1 + "s" + str(p1x) + "x" + str(p1y) + "x" + str(v) + " == " + p2 + "s" + str(p2x) + "x" + str(p2y) + "x" + str(v) + ","

f.write(combine[:-1] + ");\n")
f.flush()
f.close()
