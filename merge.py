#!/usr/bin/env python

import sys

assert(len(sys.argv) == 3)

var_mapping = {}
var_inv_mapping = {}

var_cnf_assignment = {}
var_out_assignment = {}

f_cnf = open(sys.argv[1], 'r').read().split('\n')
f_out = open(sys.argv[2], 'r').read().split('\n')

for l in f_cnf:
    if len(l) > 0 and l[0] == 'c' and ' <-> ' in l:
        l_var = l[1:].split(' <-> ')
        l_var[0] = l_var[0].strip()
        l_var[1] = l_var[1].strip()
        var_mapping[l_var[0]] = l_var[1]
        var_inv_mapping[l_var[1]] = l_var[0]

for l in f_out:
    if 'v' in l:
        l_assigns = l[1:].split(' ')
        for t_v in l_assigns:
            v = t_v.strip()
            if len(v) == 0:
                continue
            if v[0] == '-':
                var_out_assignment[v[1:]] = 'F'
            else:
                var_out_assignment[v] = 'T'

for v in var_mapping.keys():
    m = var_mapping[v]
    if m in var_out_assignment:
        var_cnf_assignment[v] = var_out_assignment[m]
        print(v + " == " + var_out_assignment[m])
