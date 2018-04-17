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

prefixes = ['s1', 's2', 's3', 's4', 's5']

for prefix in prefixes:
    f = open("20-" + prefix + "-square-internal.txt", "w")
    c = 0
    ll = prefix + "squareinternal := AND("
    for x in range(0, size):
        for y in range(0, size):
            l = prefix + "si" + str(c) + " := [1,1]("
            for v in range(0, size):
                l += prefix + "s" + str(x) + "x" + str(y) + "x" + str(v) + ","
            f.write(l[:-1] + ");\n")
            ll += prefix + "si" + str(c) + ","
            c += 1
    f.write(ll[:-1] + ");\n")
    f.flush()
    f.close()

    f = open("21-" + prefix + "-square-columns.txt", "w")
    c = 0
    ll = prefix + "squarecolumn := AND("
    for y in range(0, size):
        for v in range(0, size):
            l = prefix + "sc" + str(c) + " := [1,1]("
            for x in range(0, size):
                l += prefix + "s" + str(x) + "x" + str(y) + "x" + str(v) + ","
            f.write(l[:-1] + ");\n")
            ll += prefix + "sc" + str(c) + ","
            c += 1
    f.write(ll[:-1] + ");\n")
    f.flush()
    f.close()

    f = open("22-" + prefix + "-square-rows.txt", "w")
    c = 0
    ll = prefix + "squarerow := AND("
    for x in range(0, size):
        for v in range(0, size):
            l = prefix + "sr" + str(c) + " := [1,1]("
            for y in range(0, size):
                l += prefix + "s" + str(x) + "x" + str(y) + "x" + str(v) + ","
            f.write(l[:-1] + ");\n")
            ll += prefix + "sr" + str(c) + ","
            c += 1
    f.write(ll[:-1] + ");\n")
    f.flush()
    f.close()

    f = open("23-" + prefix + "-square-squares.txt", "w")
    c = 0
    ll = prefix + "squaresquare := AND("
    sms = square_map[size]
    for s_x in range(0, sms):
        for s_y in range(0, sms):
            for v in range(0, size):
                l = prefix + "ss" + str(c) + " := [1,1]("
                for x in range((s_x)*sms, (s_x+1)*sms):
                    for y in range((s_y)*sms, (s_y+1)*sms):
                        l += prefix + "s" + str(x) + "x" + str(y) + "x" + str(v) + ","
                f.write(l[:-1] + ");\n")
                ll += prefix + "ss" + str(c) + ","
                c += 1
    f.write(ll[:-1] + ");\n")
    f.flush()
    f.close()

f = open("99-problem.txt", "w")
assigns = ["squareinternal","squarecolumn","squarerow","squaresquare"]
rassigns = []
for prefix in prefixes:
    for a in assigns:
        rassigns.append(prefix + a)

if len(prefixes) > 1:
    rassigns.append("combine")

f.write("problem := AND(" + ",".join(rassigns) + ");\n")
f.write("ASSIGN problem;")
f.flush()
f.close()
