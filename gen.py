#!/usr/bin/env python

import sys
assert(len(sys.argv) == 2)

square_map = {}
for s in range(2, 1000):
    square_map[s*s] = s

size = int(sys.argv[1])

assert(size in square_map)

## Write header

f = open("00-header.txt", "w")
f.write("BC1.1\n")
f.flush()
f.close()

f = open("20-square-internal.txt", "w")
c = 0
ll = "squareinternal := AND("
for x in range(0, size):
    for y in range(0, size):
        l = "si" + str(c) + " := [1,1]("
        for v in range(0, size):
            l += "s" + str(x) + "x" + str(y) + "x" + str(v) + ","
        f.write(l[:-1] + ");\n")
        ll += "si" + str(c) + ","
        c += 1
f.write(ll[:-1] + ");\n")
f.flush()
f.close()

f = open("21-square-columns.txt", "w")
c = 0
ll = "squarecolumn := AND("
for y in range(0, size):
    for v in range(0, size):
        l = "sc" + str(c) + " := [1,1]("
        for x in range(0, size):
            l += "s" + str(x) + "x" + str(y) + "x" + str(v) + ","
        f.write(l[:-1] + ");\n")
        ll += "sc" + str(c) + ","
        c += 1
f.write(ll[:-1] + ");\n")
f.flush()
f.close()

f = open("22-square-rows.txt", "w")
c = 0
ll = "squarerow := AND("
for x in range(0, size):
    for v in range(0, size):
        l = "sr" + str(c) + " := [1,1]("
        for y in range(0, size):
            l += "s" + str(x) + "x" + str(y) + "x" + str(v) + ","
        f.write(l[:-1] + ");\n")
        ll += "sr" + str(c) + ","
        c += 1
f.write(ll[:-1] + ");\n")
f.flush()
f.close()

f = open("23-square-squares.txt", "w")
c = 0
ll = "squaresquare := AND("
sms = square_map[size]
for s_x in range(0, sms):
    for s_y in range(0, sms):
        for v in range(0, size):
            l = "ss" + str(c) + " := [1,1]("
            for x in range((s_x)*sms, (s_x+1)*sms):
                for y in range((s_y)*sms, (s_y+1)*sms):
                    l += "s" + str(x) + "x" + str(y) + "x" + str(v) + ","
            f.write(l[:-1] + ");\n")
            ll += "ss" + str(c) + ","
            c += 1
f.write(ll[:-1] + ");\n")
f.flush()
f.close()

f = open("99-problem.txt", "w")
f.write("problem := AND(squareinternal,squarecolumn,squarerow,squaresquare);\n")
f.write("ASSIGN problem;")
f.flush()
f.close()
